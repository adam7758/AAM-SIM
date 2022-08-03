# Simulation-Tool
The simulation tool is developed to simulate the operational process of eVTOLs over vertiport network while satisfying potential passenger demand. The detailed description of the tool is summarized in 'Simulation Tool Summary.pdf'.

# main command file
To run the simulation tool, users can run the 'SimulationPlatform.py', where parameters inculding time unit for each simulation step and simulation horizon can be revised according to user needs.

# Numerical Example
There is data for numerical study of Tampa Bay region in Florida. The input data includes 'dist.npy', 'Inputs.py', 'OD_arrivals.npy', 'pair_weight.npy' and the folder named 'Demand'. There is also default setting for eVTOL performance parameter in the file 'Entity.py'. Users can adjust the file type and parameter values accordingly.

# Demand generator
The file 'DemandGenerator.py' includes function to generate passenger arrivals at each vertiport.

# Initialization
The file 'Initialization.py' is to set up the initial state of the vertiport and eVTOLs in the network..

# State update
Files 'UserUpdate.py' and 'EvUpdate.py' inculdes functions to update passenger assignment and eVTOL states for each simulation step.

# ResultVisulization
The file 'ResultVisulization.py' includes several result visulization analysis of the numerical example. To obtain results in needs, users may need to create certain variables in corresponding files to record their values during simulation process. 
