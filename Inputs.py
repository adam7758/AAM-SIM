# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:07:22 2022

@author: zhiqiangwu
"""

import numpy as np
   
time_slot = 15 # minutes -- length of each time slots
stime = 60*6 #simulation start time
etime = 60*21 # simulation end time
slots = int((etime-stime)/time_slot) # Number of time slots,from 6:00am to 10:00pm
los1 = 10 # minutes - maximum acceptable waiting time of first arrival passengers 
los2 = 5 # minutes - maximum acceptable waiting time of last arrival passengers
los3 = 10 # minutes - maximum acceptable waiting time out-of-vehicle for arrival passengers
#los4 = 5 # number of passengers threshold waiting out-of vehicle that will triger empty vehicle dispatch
vpts = range(1,31) # indexs of vertiports


# define distance matrix
dist = np.load('dist.npy')

# Define number of vertiport capacity and evtol distribution 
max_stage = 10
min_stage = 2
max_tlof = 5
min_tlof = 2
min_ev = 2
max_ev = 8

# max_evtol = 10
OD_arrival = np.load('OD_arrivals.npy')

# Number of facility is propotional to the demand
tot_arr = [sum(i) for i in OD_arrival]
max_arr = max(tot_arr)
vpds = [int(d*max_stage/max_arr) for d in tot_arr]
vpds = [s if s >=min_stage else min_stage for s in vpds]
tlof = [int(d*max_tlof/max_arr) for d in tot_arr]
tlof = [s if s >=min_tlof else min_tlof for s in tlof]
evs = [s-2 if s-2 >= min_ev else min_ev for s in vpds]
# evs = [int(d*max_ev/max_arr) for d in tot_arr]
#evs = [s if s >=min_ev else min_ev for s in evs]
# # Expand capacity of blocked vertiport
vpds[6] = max_stage
tlof[6] = max_tlof
evs[6] = max_stage-2

# # For high value case
# vpds[10] = max_stage
# tlof[10] = max_tlof


# Generate destination probability based on vertiport pair demand
pair_weight = np.load('pair_weight.npy')
dest_prob = {}
for i in vpts:
    dest_prob['v'+str(i)] = list(pair_weight[i-1,:])