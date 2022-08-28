# AAM-SIM
The simulation tool, AAM-SIM, is developed to simulate the operational process of eVTOLs over vertiport network while satisfying potential passenger demand. The detailed description of the tool is summarized in 'Simulation Tool Summary.pdf'. Briefly speaking, given UAM network and potential passenger demand, AAM-SIM defines the operational rules of eVTOLs and dispatch them arocss vertiports in the network to transportation passengers from origins to their destinations. AAM-SIM is able to provide us insignts including but not limited to eVTOL operation characteristics, UAM network bottle necks, service quality and system energy requirements. 

# main command file
The main command file for AAM-SIM tool is 'SimulationPlatform.py', which calls for functions to update vertiport, aircrafts and passengers status for each time step of simulation. The tool user can also adjust parameters such as time unit for each simulation step and simulation horizon according to their needs.

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
