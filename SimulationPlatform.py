# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:37:44 2020

@author: zhiqiangwu

Function:
    This section defines the simulation process of the platform
"""

from Inputs import *
from Initialization import vert_init1, vert_init2
from EvUpdate import ev_update
from UserUpdate import user_update
import time
import matplotlib.pyplot as plt
# Initialize the user arrival and vertiport and evtol configuration
ini_out = vert_init1(vpts,vpds,tlof,slots,evs,stime,etime)
vertiports = ini_out['vpts']
arrivals = ini_out['arrs']

#evtols = ini_out['evs']
# total_demand = [arrivals['arr'+str(i)]['demand'] for i in range(1,31)]
# total_demand = sum(total_demand)
# Generate probability of destinations for users at each vertiport
# demand = [arrivals['arr'+str(vpt)]['demand'] for vpt in vpts]
# dest_prob = vp_demand(demand,vpts)

#start_time = time.time()

timer1 = 0
timer2 = 6*60
user_id = 1
seed1 = 1
seed2 = 100
served_users = []
unserved_users = []

v_stage = {}
v_tlof = {}
v_cSoC = {}
v_eSoC = {}
v_eusage = {}
for v in vpts:
    
    v_stage['v'+str(v)]=[]
    v_tlof['v'+str(v)]=[]
    v_cSoC['v'+str(v)]=[]  # SoC charged
    v_eSoC['v'+str(v)]=[]  # end of charge SoC
    v_eusage['v'+str(v)]=[] # power usage at each vertiport
    

ene_consum = []
for slot in range(slots):
    # Generate user arrival for each vertiport at each time slot
    timer1 = time_slot*slot + 6*60
    output = vert_init2(vpts,time_slot,slot,timer1,user_id,vertiports,dest_prob,arrivals,seed1,seed2)
    vertiports = output['vertiports']
    user_id = output['user_id']
    seed1 += 10000
    seed2 += 10000
        
    # Simulate evtol operation process
    for t in range(time_slot):
        timer2 += 1
        for vpt in vpts:
            output1 = user_update(vpt,vertiports,timer2)
            
            vertiports = output1['vertiports']
            ene_charged1 = output1['ene_charged'] # energe charged for each eVTOL
            eSoC1 = output1['eSoC']
            unserved_users = unserved_users + output1['unserved_users']
            
            output2 = ev_update(vpt,vertiports)
            
            vertiports = output2['vertiports']
            new_users = output2['served_users']
            ene_charged2 = output2['ene_charged']
            elec_usage = output2['elec_usage']
            eSoC2 = output2['eSoC']
            ene_consum.append(output2['ene_consumed'])
            
            served_users = served_users + new_users
            vertiport = vertiports['v'+str(vpt)] 
            
            v_stage['v'+str(vpt)].append(vertiport.stage/vertiport.n_cap)
            v_tlof['v'+str(vpt)].append(vertiport.tlof/vertiport.n_tlof)
            v_cSoC['v'+str(vpt)] = v_cSoC['v'+str(vpt)] + ene_charged1 + ene_charged2
            v_eSoC['v'+str(vpt)] = v_eSoC['v'+str(vpt)] + eSoC1 + eSoC2
            v_eusage['v'+str(vpt)].append(elec_usage)
#end_time = time.time()
#ex_time = end_time - start_time






