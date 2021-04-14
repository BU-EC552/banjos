from celloapi2 import CelloResult, CelloQuery

# Ask user for input files:
# 1) verilog file that describes genetic circuit
# 2) UCF file that describes target vector
# 3) file that describes input signals
# 4) file that describes output signal

# call CelloQuery to obtain design space

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

