# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 08:25:11 2022

@author: zhiqiangwu
"""
from Inputs import vpts
from SimulationPlatform import *
from DemandGenerator import arr_gen

import numpy as np
import matplotlib.pyplot as plt
# Performance evaluation                            
swait = [user.s_wait for user in served_users]
iwait =  [user.i_wait for user in served_users]
# iwait =  [user.i_wait for user in served_Passengers if user.i_wait >0]            
touthold = [user.touthold for user in served_users if user.touthold >0]            
lhold = [user.lhold for user in served_users if user.lhold >0]
tinhold = [user.tinhold for user in served_users if user.tinhold >0] 


# Identify blocked vertiports

# stage_pads = [vertiports['v'+str(v)].stage for v in vpts]
# s_index = [i for i,e in enumerate(stage_pads) if e==0]
# tlof_pads = [vertiports['v'+str(v)].tlof for v in vpts]
# t_index = [i for i,e in enumerate(tlof_pads) if e==0]
# user_iwait = [user for user in served_Passengers if user.i_wait>=10]

# # # Demand distribution
# for i,v in enumerate(arrivals):
#     count = arrivals[v]['count']
#     plt.plot(count)
# plt.xlabel('Time (15 minutes)')
# plt.ylabel('Number of Passengers arrivals for each 15 minutes')
# plt.title('Plot of Passengers Arrival Distribution for '+str(i+1)+' Vertiport')
# plt.grid(True)
# plt.show()

# Total Demand of each vertiport
demand = [list(np.load('Demand/arr_v'+str(i)+'.npy')) for i in vpts]
demand = [arr_gen(arr,60,60*6,60*21)['demand'] for arr in demand]


# Service quality visualization
n, bins, patches = plt.hist(swait, 10,facecolor='g', alpha=0.75)
plt.xlabel('Waiting time (min)')
plt.ylabel('Number of Passengers')
plt.title("Histogram of " + str(len(swait)) + " Passengers' in-vehicle Waiting Time")
# plt.grid(True)
plt.show()

n, bins, patches = plt.hist(iwait, 10,facecolor='g', alpha=0.75)
plt.xlabel('Waiting time (min)')
plt.ylabel('Number of Passengers')
plt.title("Histogram of " +str(len(iwait)) + " Passengers' out-of-Vehicle Waiting Time")
# plt.grid(True)
plt.show()

n, bins, patches = plt.hist(lhold, 20,facecolor='g', alpha=0.75)
plt.xlabel('Holding time (min)')
plt.ylabel('Number of Passengers')
plt.title("Histogram of " + str(len(lhold))+" Passengers' landing holding time")
# plt.grid(True)
# plt.xlim([0,25])
plt.show()

n, bins, patches = plt.hist(tinhold, 10,facecolor='g', alpha=0.75)
plt.xlabel('Holding time (min)')
plt.ylabel('Number of Passengers')
plt.title("Histogram of " + str(len(tinhold))+" Passengers' taxi-in holding time")
# plt.grid(True)
plt.show()

n, bins, patches = plt.hist(touthold, 10,facecolor='g', alpha=0.75)
plt.xlabel('Holding time (min)')
plt.ylabel('Number of Passengers')
plt.title("Histogram of " + str(len(touthold))+" Passengers' taxi-out holding time")
# plt.grid(True)
plt.xlim([0,5])
plt.show()


# Group vertiports based on demand
vert_order = [i for _,i in sorted(zip(demand,list(vpts)),reverse=True)]
vpts1 = vert_order[0:5]
vpts2 = vert_order[5:10]
vpts3 = vert_order[10:15]
vpts4 = vert_order[15:20]
vpts5 = vert_order[20:25]
vpts6 = vert_order[25:30]
# vpts2 = range(6,11)
# vpts3 = range(11,16)
# vpts4 = range(16,21)
# vpts5 = range(21,26)
# vpts6 = range(26,31)
vpts_slot=[vpts1,vpts2,vpts3,vpts4,vpts5,vpts6]


# for i,v in enumerate(arrivals):
#     for j in range(1,6):
        
#         count = arrivals[v]['count']
#         plt.plot(count)
#     plt.xlabel('Time (15 minutes)')
#     plt.ylabel('Number of Passengers arrivals for each 15 minutes')
#     plt.title('Plot of Passengers Arrival Distribution for '+str(i+1)+' Vertiport')
#     plt.grid(True)
#     plt.show()       


# stage_ocu = [v_stage['v'+str(v)] for v in vpts]
# plt.boxplot(stage_ocu)
# plt.xlabel('Vertiport Index')
# plt.ylabel('Ratio of Available Pads')
# plt.title('Statistics Comparison for Parking Pads Occupation at Vertiports')
# plt.show()  

 

for i,vs in enumerate(vpts_slot):
    for v in vs:
        plt.plot(v_stage['v'+str(v)])
    plt.xlabel('Time(min)')
    plt.ylabel('Ratio of Available Pads')
    plt.title('Group'+str(i+1))
    plt.show()    

# TLOF_ocu = [v_tlof['v'+str(v)] for v in vpts]
# plt.boxplot(TLOF_ocu)
# plt.xlabel('Vertiport Index')
# plt.ylabel('Ratio of Available TLOF')
# plt.title('Statistics Comparison for TLOF Occupation at Vertiports')
# plt.show() 

for i,vs in enumerate(vpts_slot):
    for v in vs:
        plt.plot(v_tlof['v'+str(v)])
    plt.xlabel('Time(min)')
    plt.ylabel('Ratio of Available TLOF')
    plt.title('Group'+str(i+1))
    plt.show()

for i,vs in enumerate(vpts_slot):
    for v in vs:
        plt.plot(v_eusage['v'+str(v)])
    plt.xlabel('Time(min)')
    plt.ylabel('Power Usage (kWh)')
    plt.title('Group'+str(i+1))
    plt.show()

for i,vs in enumerate(vpts_slot):
    for v in vs:
        plt.plot(v_cSoC['v'+str(v)])
    plt.xlabel('eVOLs')
    plt.ylabel('SoC')
    plt.title('Group'+str(i+1))
    plt.show()  

# Draw the digital map of the network
v_coords = np.load('v_coords.npy')
x,y = v_coords.T
color = [1]*30
# area = demand
# def netvisual(color,area):    
#     plt.scatter(x,y, s= demand,c=color)
#     plt.rcParams['figure.figsize'] = [8,10]
#     figure = plt.gca()
#     x_axis = figure.axes.get_xaxis()
#     x_axis.set_visible(False)
#     y_axis = figure.axes.get_yaxis()
#     y_axis.set_visible(False)
#     plt.title('Relative locations of vertiports (size proportial to the demand)')
#     plt.show()

# Identify the blocks at vertiport due to full occupation of staging pads and TOFL
sta_block = [v_stage['v'+str(v)].count(0) for v in vpts]
TOFL_block = [v_tlof['v'+str(v)].count(0) for v in vpts]
# Identify vertiports with severe block time
sta_id = [idx for idx, ele in enumerate(sta_block) if ele>=500]
tofl_id = [idx for idx, ele in enumerate(TOFL_block) if ele>=500]
# netvisual(sta_block,area)
# netvisual(TOFL_block,area)

plt.scatter(x,y, s= demand,c=sta_block)
plt.rcParams['figure.figsize'] = [8,10]
figure = plt.gca()
x_axis = figure.axes.get_xaxis()
x_axis.set_visible(False)
y_axis = figure.axes.get_yaxis()
y_axis.set_visible(False)
plt.title('Relative locations of vertiports (size proportial to the demand)')
for i in sta_id:
    plt.text(x[i]-5000,y[i],'Block time from staging pads:'+str(sta_block[i]))
for i in tofl_id:
    plt.text(x[i]-5000,y[i]-2500,'Block time from TOFL:'+str(TOFL_block[i]))
plt.show()

# # Plot results in one figure
# for v in vpts:
#     plt.plot(v_stage['v'+str(v)])
# plt.xlabel('Time(min)')
# plt.ylabel('Ratio of Available Pads')
# plt.title('Ratio of Available Parking Pads at Vertiports')
# plt.show()  


# for v in vpts:
#     plt.plot(v_tlof['v'+str(v)])
# plt.xlabel('Time(min)')
# plt.ylabel('Ratio of Available TLOF')
# plt.title('Ratio of Available Takeoff and Landng at Vertiports')
# plt.show()  
    
# for v in vpts:
#     plt.plot(v_eusage['v'+str(v)])
# plt.xlabel('Time(min)')
# plt.ylabel('Power Usage (kWh)')
# plt.title('Power Usage at Vertiports')
# plt.show()
    

# for v in vpts:
#     plt.plot(v_cSoC['v'+str(v)])
# plt.xlabel('eVOLs')
# plt.ylabel('SoC')
# plt.title('SoC charged before Serving Passengers')
# plt.show() 

# for v in vpts:
#     plt.plot(v_eSoC['v'+str(v)])
# plt.xlabel('eVOLs')
# plt.ylabel('SoC')
# plt.title('SoC before Serving Passengers')
# plt.show() 
    