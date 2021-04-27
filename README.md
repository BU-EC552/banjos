![logo](https://user-images.githubusercontent.com/57968955/116004476-cada0b00-a5d0-11eb-8d07-da368cd8bfe6.png)
## B.A.N.G.O.S  

BANGOS is a command line tool that interacts with the CELLO API. It takes a circuit (defined in verilog) to perform sensitivity analysis using stochastic simulation to determine how sensitive the parameters of the input signals are to gaussian noise. Aside from the parameter perturbation - sensitivity analysis plots, the circuit will be scored with a BANGO Factor that uses user-inputted weights for an objectove function that depends on the following elements:
- behavior metric (CELLO score)
- assembly metric (gc content)
- cost (based on biological parts registries) 
-  circuit toxicity. 

The BANGO score lies in a range from 0 to 1, where a circuit that obtains a score closer to 1 represents a robust circuit in the presence of noise, an easier circuit to build and lastly an inexpensive circuit where its parts already exist in the registry. 

### Installation 
Please make sure that you can run the cello api on your machine. To install cello, please follow the instructions described in: https://github.com/CIDARLAB/celloapi2

Aside from the cello api requirenments, no further dependencies are necessary. 

To install BANGOS, clone this repository. 

### Running BANGOS

`python3 main.py input`

You will be asked to specify your preference for the weighting scheme: which metrics matter most to you, as well as the name of your circuit (for example: and.v) and the number of input signals your circuit needs. 

Please make sure that your input folder contains:
- INPUT JSON file
- UCF JSON file
- OUTPUT JSON file
- verilog file that describes your circuit 



