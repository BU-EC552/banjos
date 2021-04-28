![logo](https://user-images.githubusercontent.com/57968955/116004476-cada0b00-a5d0-11eb-8d07-da368cd8bfe6.png)
## B.A.N.G.O.S  

BANGOS is a command line tool that interacts with the CELLO API. It takes a circuit (defined in verilog) to perform sensitivity analysis using stochastic simulation to determine how sensitive the parameters of the input signals are to gaussian noise. Aside from the parameter perturbation - sensitivity analysis plots, the circuit will be scored with a BANGO Factor that uses user-inputted weights for an objectove function that depends on the following elements:
- behavior metric (CELLO score)
- assembly metric (gc content)
- cost (based on biological parts registries) 
-  circuit toxicity. 

The BANGO score lies in a range from 0 to 1, where a circuit that obtains a score closer to 1 represents a robust circuit in the presence of noise, an easier circuit to build and lastly an inexpensive circuit. 

### Installation 
Please make sure that you can run the cello api on your machine. To install cello, please follow the instructions described in: https://github.com/CIDARLAB/celloapi2

Please move to the CODE directory. The CODE folder is available in Final_Project_BANGOS

Next, to install the remaining dependencies, please run 
`pip3 install -r requirements.txt`

For the cost metric, BANGOS uses the iGEM's Registry of Standard Biological Parts at: http://parts.igem.org/Registry_API, however this file was modified for the purpose of the software developement.

Download modified XML file to your directory here. https://drive.google.com/file/d/1DIQIdmrU2aYTFxdpX7-2oLN5a5YmRYYl/view?usp=sharing
Please make sure to move this file to the CODE directory

To install BANGOS, clone this repository. 

### Running BANGOS

`python3 main.py input`

You will be asked to specify your preference for the weighting scheme: which metrics matter most to you, as well as the name of the device(for example: Eco1C1G1T1), your circuit (for example: and.v) and the number of input signals your circuit needs. 

Please make sure that your input folder contains AND is within the CODE directory:
- INPUT JSON file
- UCF JSON file
- OUTPUT JSON file
- verilog file that describes your circuit 


** In the CODE directory, you will see an example of the structure of the input folder needed.


