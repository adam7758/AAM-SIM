# How to Cite AAM-SIM Source Code?
Wu, Z. & Zhang, Y (2022). AAM-SIM source code (Version 1.0), A Simulation Platform for On-Demand Advanced Air Mobility, Smart Urban Mobility Lab at the University of South Florida, http://www.github.com/adam7758/AAM-SIM. 

# AAM-SIM
The simulation tool, AAM-SIM, is developed to simulate the operational process of eVTOLs over vertiport network while satisfying potential passenger demand. The detailed description of the tool is summarized in 'Simulation Tool Summary.pdf'. Briefly speaking, given an AAM network and potential passenger demand, AAM-SIM defines the operational rules of AAM service and dispatches eVTOLs across vertiports in the network to transport passengers from their origins to destinations. AAM-SIM is able to provide system performance measures such as passenger travel time and waiting time, eVTOLs load factor, eVTOL state of charge, vertiport occupancy and charging capacity. Besides service quality and system energy requirements, AAM-SIM can also point out the bottlenecks of the AAM network and allows the exploration of strategies to mitigate the bottlenecks. 

# Main command file
The main command file for AAM-SIM tool is 'SimulationPlatform.py', which commits the command for the entire simulation run and calls for functions to update vertiport, eVTOL and passenger status for each timestamp of the simulation. The tool user can adjust time unit and simulation horizon according to their needs.

# Demand generator
The file 'DemandGenerator.py' includes function to generate passenger arrivals at each vertiport, generating both overall distribution as well as exact arrivals.

# Initialization
The file 'Initialization.py' is to set up the initial state of the vertiport and eVTOLs in the network, namely defining the initial distribution of eVTOLs and number of facilities (take-off and landing pads, staging/charging pads) at each vertiport.

# State update
Files 'UserUpdate.py' and 'EvUpdate.py' inculdes functions to update passenger assignment and eVTOL states for each simulation timestamp. The detailed state definition and state change rule can be found in 'Simulation Tool Summary.pdf'.

# ResultVisulization
The file 'ResultVisulization.py' includes several result visulization analysis of the numerical example. To obtain results in needs, users may need to create certain variables in corresponding files to record their values during simulation process. 

# Numerical Example
There is data for numerical study of Tampa Bay region in Florida. The input data files include 'dist.npy', 'Inputs.py', 'OD_arrivals.npy', 'pair_weight.npy' and the folder named 'Demand'. There is also default setting for eVTOL performance parameter in the file 'Entity.py'. Specifically, 'Inputs.py' defines initial parameter setting for the network, including initial number of aircrafts, TOFL and staging pads at each vertiport; 'dist.npy' represent distance matrix of the vertiport;'OD_arrivals.npy' indicates number of arrivals for each vertiport; 'pair_weight.npy' contains route demand weight for each pair of vertiport.
