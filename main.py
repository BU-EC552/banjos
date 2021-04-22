from celloapi2 import CelloResult, CelloQuery
import sys
import os

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
q = CelloQuery(
    input_directory=in_dir,
    output_directory=out_dir,
    verilog_file=v_file,
    compiler_options=options,
    input_ucf=in_ucf,
    input_sensors=input_sensor_file,
    output_device=output_device_file,
)

q.get_results()
res = CelloResult(results_dir=out_dir)
print(res.circuit_score)

#################### NEXT STEP #########################
# send design space to stochastic simulation algorithm

# obtain simulation data

# perform optimization to obtain consistent circuit response (eg minimize variance)
# parameter perturbation will be performed to assess robutness of circuit (eg sensitivity analysis)

# evaluate circuit with different metrics:
# 1) CelloResult score?
# 2) Cello toxicity?

# access part registry
# 3) part manufacturing cost

# set default values for comparison : eg normal gc content in order to make comparison
# 4) assembly cost

# sensitivity plots

# overall circuit score and robustness

