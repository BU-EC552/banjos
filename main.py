# imports:
import statistics
from cmath import sqrt

from celloapi2 import CelloResult, CelloQuery
import sys
import matplotlib.pyplot as plt
from helper import *
from itertools import combinations
import pandas as pd

# Ask user for input files:
# 1) verilog file that describes genetic circuit
# 2) UCF file that describes target vector (default = Eco1C1G1T1)
# 3) file that describes input signals (default = Eco1C1G1T1)
# 4) file that describes output signal (default = Eco1C1G1T1)

'''For now, this tool is a command-line feature. Users will enter important
files using command line. User will enter path to directory of input files'''
# Example of command input:
# python3 main.py input

print("Hello User, B.A.N.G.O.S will evaluate your circuit based on its performance using Cello, "
      "circuit toxicity, and an estimate of part manufacturing cost as well as an assembly cost")
print("Please provide us with what metrics are most important to you, if all are the same please "
      "put 1, else write 1 to 4 next to each metric")
w1 = input("Cello Performance: ")
w2 = input("Circuit Toxicity: ")
w3 = input("Part Manufacturing Cost: ")
w4 = input("Assembly cost: ")

# normalize weight (so they sum to unity)
total_sum = int(w1) + int(w3) + int(w4)
weight1 = int(w1)/total_sum
# weight2 = int(w2)/total_sum
weight3 = int(w3)/total_sum
weight4 = int(w4)/total_sum

# Getting directory of input files
directory = sys.argv[1]

# call CelloQuery to obtain design space
# Set our directory variables.
in_dir = os.path.join(os.getcwd(), 'input')
out_dir = os.path.join(os.getcwd(), 'output')

print("Thank You for providing your preferences")
print("Now tell us the name of the chassis were you want to build your circuit and your circuit ")
# Set our input files.
# ask user for the chassis the circuit is going to be constructed
chassis_name = input("Chassis name: ")
in_ucf = f'{chassis_name}.UCF.json'
# ask user for verilog file describing circuit
v_file = input("Circuit to test: ")
options = 'options.csv'
input_sensor_file = f'{chassis_name}.input.json'
output_device_file = f'{chassis_name}.output.json'

# ask user how many input signals circuit needs
signal_input = input("Number of input signals needed: ")
signal_input = int(signal_input)
# initialize to zero
best_score = 0
best_input_signals = None

q = CelloQuery(
    input_directory=in_dir,
    output_directory=out_dir,
    verilog_file=v_file,
    compiler_options=options,
    input_ucf=in_ucf,
    input_sensors=input_sensor_file,
    output_device=output_device_file,
)
signals = q.get_input_signals()
signal_pairing = list(combinations(signals, signal_input))
for signal_set in signal_pairing:
    signal_set = list(signal_set)
    q.set_input_signals(signal_set)
    # OBTAIN RESULTS FROM CELLO
    q.get_results()
    # Fetch our Results.
    try:
        res = CelloResult(results_dir=out_dir)
        if res.circuit_score > best_score:
            best_score = res.circuit_score
            best_input_signals = signal_set
    except:
        pass
    q.reset_input_signals()
print(f'Score: {best_score}')
print(f'Best input signals: {best_input_signals}')

# dealing with cello's stochastic score: create average of score with best input signals
# evaluate circuit with different metrics:
# 1) CelloResult score
scores = []
for i in range(5): # 5 for now... probably need more runs or justify why 5?
  q.set_input_signals(best_input_signals)
  q.get_results()
  res = CelloResult(results_dir=out_dir)
  scores.append(res.circuit_score)
  # print(f'Score is: {res.circuit_score}')

# average score:
avg_score = 0
scores.append(best_score)
for i in range(len(scores)):
    avg_score = avg_score + scores[i]
avg_score = avg_score/6
print(f"Average score with best input signals: {avg_score}")
# standard deviation:
std = statistics.pstdev(scores)
print(f'Standard deviation: {std}')

# parameter perturbation will be performed to assess "robustness" of circuit (eg sensitivity analysis)
rob_scores = []
input_parameters = parseInput(in_dir + '/' + input_sensor_file)
# copy of unpertubed input parameters to reset after each parameter is perturbed
noiseless_param = parseInput(in_dir + '/' + input_sensor_file)
signal_keys = list(input_parameters.keys())
for i in range(signal_input):
    for j in range(len(signal_keys)):
        if best_input_signals[i]+'_sensor_model' == signal_keys[j]:
            print(f'Evaluating signal: {best_input_signals[i]}')
            # each parameter of input signal at a time
            for n in range(4):
                # select "perturbations" from normal distribution - each "noise" has its own distribution
                # (multiply) the parameters from input signals to simulate noise
                num = get_truncated_normal(mean=0.5, sd=1, low=0, upp=1)
                input_parameters[best_input_signals[i] + '_sensor_model'][n]['value'] = input_parameters[best_input_signals[i] + '_sensor_model'][n]['value'] * (num.rvs(1))[0]
                # write modified value to new json file to submit to cello
                new_file = f'signal{i}_parameter{n}.input.json'
                # exporting to json
                output_json(input_sensor_file, input_parameters, in_dir, new_file)
                print(f'Evaluating parameter: {n}')
                # submit to cello to measure "robustness" - how score changes
                m = CelloQuery(
                    input_directory=in_dir,
                    output_directory=out_dir,
                    verilog_file=v_file,
                    compiler_options=options,
                    input_ucf=in_ucf,
                    input_sensors=new_file,
                    output_device=output_device_file,
                )
                # set input signals to be the best two found before
                m.set_input_signals(best_input_signals)
                # get results
                m.get_results()
                res = CelloResult(results_dir=out_dir)
                rob_scores.append(res.circuit_score)
                # reset value
                input_parameters[best_input_signals[i] + '_sensor_model'][n]['value'] =  noiseless_param[best_input_signals[i] + '_sensor_model'][n]['value']

# analysis of scores --> order: (ymax, ymin, alpha, beta) --> for each signal
delta_scores = []
for i in range(len(rob_scores)):
    delta_scores.append(rob_scores[i] - avg_score)
# print(delta_scores)
# figure 1 = plot delta for each parameter perturbation score
plt.subplot(1,2,1)
plt.plot(delta_scores)
plt.ylabel("Delta Values: How scores changed with noise")
plt.xlabel("Parameters")
plt.title("Input Signals - Sensitivity Analysis")
# figure 2 plot scores vs original scores and add "error" bars
original_score = []
best_scores = []
pos_stds = []
neg_stds = []
for i in range(len(rob_scores)):
    original_score.append(avg_score)
    best_scores.append(best_score)
    pos_stds.append(avg_score+std)
    neg_stds.append(avg_score-std)
plt.subplot(1,2,2)
plt.plot(best_scores, 'b', original_score, 'g', rob_scores, 'r', pos_stds, 'y', neg_stds, 'y')
plt.xlabel("Parameters")
plt.ylabel("Scores")
plt.legend(["Best Score", "Average Score", "Parameter Perturbation Scores", "Standard Dev", "Standard Dev"])
plt.show()

# display more info - eg whether is lies in standard deviation of scores for each input signal:
# make all delta values positive:
pos_delta = [abs(ele) for ele in delta_scores]
labels = []
for i in range(len(delta_scores)):
    if delta_scores[i] > std:
        labels.append('yes')
    else:
        labels.append("No")
name_params = []
for i in range(signal_input):
    name_params.extend(['ymax', 'ymin', 'alpha', 'beta'])
df1 = pd.DataFrame(list(zip(name_params, labels)),
               columns =['Parameter Perturbation', 'Outside of standard deviation?'])
print(df1)

# evaluate circuit with different metrics:
# 2) Cello toxicity. Toxicity result after CelloResult
res_toxic = findToxicity()


# 3) part manufacturing cost
# Simulate cost. If part exists, cost += 0, else cost += 1
# Reads the xml_parts.xml to get all known parts.
knownParts = readXMLparts('xml_parts.xml')
fileInputJson = f'input/{chassis_name}.input.json'
userParts = getPartsFromInputJson(fileInputJson)
cost = 0
for part in userParts:

    if part not in knownParts.keys():
       # Increment cost
       cost += 1
       print("Part does not exists...")
fileUCFJson = f'input/{chassis_name}.UCF.json'
userParts2 = getPartsFromInputJson(fileUCFJson)
for part in userParts2:

    if part not in knownParts.keys():
       # Increment cost
       cost += 1
       print("Part does not exists...")

print('Total cost for this design: ', cost)

# set default values for comparison : eg normal gc content in order to make comparison
# 4) assembly cost:
# call cg content function if > 60 % --> high cost
# get DNA sequences
sequences1 = userParts.values()
sequences2 = userParts2.values()
gc_cost1 = 0
gc_cost2 = 0
for seq in sequences1:
    temp = GC_function(seq)
    gc_cost1 += temp
gc_cost1 = gc_cost1/len(sequences1)
for seq in sequences2:
    temp = GC_function(seq)
    gc_cost2 += temp
gc_cost2 = gc_cost2/len(sequences2)
total_gc = gc_cost1 + gc_cost2/2

# overall circuit score and robustness
# make chart with all costs and overall score with user inputted weights
obj_func = 0
# ignore toxicity fo now
obj_func = (weight1 * avg_score)  - (weight3 * cost) - (weight4 * total_gc)
df = pd.DataFrame({'Score': avg_score, 'Toxicity': res_toxic, 'Parts Cost': cost, 'Assembly Cost': total_gc, 'Overall Performance': obj_func})
print(df)

