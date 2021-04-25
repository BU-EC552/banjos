# imports:
from celloapi2 import CelloResult, CelloQuery
import sys
import matplotlib.pyplot as plt
from helper import *
from itertools import combinations
from inspect import signature

# Ask user for input files:
# 1) verilog file that describes genetic circuit
# 2) UCF file that describes target vector
# 3) file that describes input signals
# 4) file that describes output signal

'''For now, this tool is a command-line feature. Users will enter important
files using command line. User will enter path to directory of input files'''
# Example of command input:
# python3 main.py input

# Getting directory of input files
directory = sys.argv[1]

# call CelloQuery to obtain design space
# Set our directory variables.
in_dir = os.path.join(os.getcwd(), 'input')
out_dir = os.path.join(os.getcwd(), 'output')

# Set our input files.
chassis_name = 'Eco1C1G1T1'
in_ucf = f'{chassis_name}.UCF.json'
v_file = 'and.v'
options = 'options.csv'
input_sensor_file = f'{chassis_name}.input.json'
output_device_file = f'{chassis_name}.output.json'

# READ FROM VERILOG FILE the NUMBER OF INPUT SIGNALS NEEDED
signal_input = 2
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
# score = 0
# for i in range(5): # 5 for now... probably need more runs or justify why 5?
  #  q.set_input_signals(best_input_signals)
  #  q.get_results()
   # res = CelloResult(results_dir=out_dir)
   # score = score + res.circuit_score
    # print(res.circuit_score)

# avg_score = score/5
# print(avg_score)

#################### NEXT STEP #########################
# send design space to stochastic simulation algorithm

# obtain simulation data

# perform optimization to obtain consistent circuit response (eg minimize variance)
# extract parameters to optimize from UCF file
# ucf_parameters = parseInput(in_dir + '/' + in_ucf)
# num_parameters = len(ucf_parameters)


# parameter perturbation will be performed to assess "robustness" of circuit (eg sensitivity analysis)
rob_scores = []
input_parameters = parseInput(in_dir + '/' + input_sensor_file)
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
                new_file = 'noise.input.json'
                # currently not properly exporting json (missing info that is not included in parseInput
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

# analysis of scores --> order: (ymax, ymin, alpha, beta) --> for each signal
delta_scores = []
for i in range(len(rob_scores)):
    delta_scores.append(rob_scores[i] - best_score)
# plot sensitiviy analysis
plt.plot(delta_scores)
plt.ylabel("Delta Values: How scores changed with noise")
plt.xlabel("Parameters")
plt.title("Input Signals - Sensitivity Analysis")
plt.show()
# do more analysis
print(delta_scores)
# evaluate circuit with different metrics:
# 1) CelloResult score?
# 2) Cello toxicity?

# access part registry
# 3) part manufacturing cost

# set default values for comparison : eg normal gc content in order to make comparison
# 4) assembly cost

# sensitivity plots

# overall circuit score and robustness