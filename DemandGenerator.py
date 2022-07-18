# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:07:58 2022

@author: zhiqiangwu
"""

# Generate potential demand based on a binomial distribution based on summation of three normal distribution
#  one centered at 8 hours (8:00 am) with a standard deviation of 2 hours, another centered at 16 hours (4:00 pm) 
# with a standard deviation of 2 hours, and a third centered at 12 hours (noon) with a standard deviation of 6 hours.

import numpy as np

def arr_gen(arr,slots,stime,etime):
    
    
    # consider arrivals during study horion
    arrs = [i for i in arr if i in range(stime,etime+1)] 
    
    count, bin_edges = np.histogram(arrs,bins=slots) # demand for each 15 minutes
    demand = len(arrs)
    arrival = {'demand':demand,'count':count}

    return arrival

# Generate a possion arrival process for each slot
def poisson_arr(count,slot,seed):
    
    np.random.seed(seed)
    intervals = np.random.poisson(lam=slot/(count+1), size= count).tolist()
    
    return intervals

# Random generate user destination based on probability
def dest_draw(prob,seed):
    np.random.seed(seed)
    p = np.random.rand()
    prob_ac = [sum(prob[0:i]) for i in range(1,len(prob)+1)]
    
    verp = prob.index(max(prob))
    for v,p1 in enumerate(prob_ac):
        if p <= p1:
            verp = v
            break
    
    return verp