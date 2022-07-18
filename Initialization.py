# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:08:28 2022

@author: zhiqiangwu
"""

from Entity import vertiport,user,eVTOL
from DemandGenerator import arr_gen , poisson_arr,dest_draw
import numpy as np
def vert_init1(vpts,vpds,tlof,slots,evs,stime,etime):
    
    # Initialize vertiport configuration and user arrival
    vertiports = {}
    arrivals = {}
    
    
    for vpt in vpts:
        vertiports['v'+str(vpt)] = vertiport(vpt,vpds[vpt-1],tlof[vpt-1])
        arr = np.load('Demand/arr_v'+str(vpt)+'.npy')
        arr = list(arr)
        arrivals['arr'+str(vpt)] = arr_gen(arr,slots,stime,etime)
        
        
    # Initialize evtol configuration
    ev_id = 0
    evtols = {}
    for vpt, ev in enumerate(evs):
        for ind in range(ev):
            ev_id = ev_id + 1
            evtol = eVTOL(ev_id)
            evtols['ev'+str(ev_id)] = evtol
            vertiports['v'+str(vpt+1)].add_eVTOL(evtol)
    for vpt in vpts:
        vertiports['v'+str(vpt)].stage = vertiports['v'+str(vpt)].n_cap-len(vertiports['v'+str(vpt)].eVTOLs)            
    ini_out ={'vpts':vertiports,'arrs':arrivals,'evs':evtols}
    
    return ini_out
    
def vert_init2(vpts,time_slot,slot,timer,user_id,vertiports,dest_prob,arrivals,seed1,seed2):
    for vpt in vpts:
        
        slot_count = arrivals['arr'+str(vpt)]['count'][slot] # number of arrivals at each time slot
        if slot_count == 0:
            continue
            
        intervals = poisson_arr(slot_count,time_slot,seed1) # arrival intervals for each user
        acc_inter = [timer+sum(intervals[0:i]) for i in range(1,slot_count+1)]
        prob = dest_prob['v'+str(vpt)]
        
        for u in range(slot_count):
            verp = dest_draw(prob,seed2)
            user_setup = user(user_id,vpts[verp],acc_inter[u])
            vertiports['v'+str(vpt)].add_user(user_setup)
            user_id = user_id + 1
            seed2 += 1
            
        seed1 += 1
        
    output = {'vertiports':vertiports,'user_id':user_id}   
     
    return output