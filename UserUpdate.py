# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 02:48:32 2021

@author: zhiqiangwu
"""

from Inputs import dist,los3
def user_update(vpt,vertiports,timer):
    ec_SoC = [] # energy charged
    eSoC = []  # end of charge SoC
    o_vertiport = vertiports['v'+str(vpt)]
    # Check and update status of users
    users = o_vertiport.users
    evtols = o_vertiport.eVTOLs
    unserved = []

    for u in users:
        if u.i_wait > los3:
            users.remove(u)
            unserved.append(u)
            continue
        if u.arr_time <= timer: #what is the condition for?
            
            # check for available evtol 
            for e in evtols:                
                cruise_time = int(60*dist[vpt-1,u.dest-1]/e.speed)
                
                # check the status of each evtol
                if e.state == 1 and e.dest == u.dest and len(e.users) < e.capacity:                  
                    users.remove(u)
                    u.evtol = e
                    e.add_user(u)
                    break
                    
                elif e.state == 0:
                    users.remove(u)
                    u.evtol = e
                    e.dest = u.dest
                    e.add_user(u)
                    e.cruise = cruise_time
                    e.state_change()
                    break
                                    
                elif e.state == 8 and e.SoC >= cruise_time*e.ene_cruise+e.ene_takeoff+e.ene_land+e.reserve:
                    users.remove(u)
                    u.evtol = e
                    e.dest = u.dest
                    e.add_user(u)
                    e.cruise = cruise_time
                    e.state = 1
                    e.eSoC = e.SoC
                    e.cSoC = e.eSoC - e.sSoC
                    ec_SoC.append(e.cSoC)
                    eSoC.append(e.eSoC)
                    
                    break
                
            if u in users: # if user is not assigned to any evtol
                u.add_iwait()                   
    
                # # Add eVTOL dispatch strategies
                # if u.iwait >= los3:
                #     for vpt2 in vertiports:
                #         v_current = 'v'+str(vpt)
                #         if vpt2 != v_current:
                #             evs = vertiports[vpt2]
                #             ev_0state = 0
                #             for ev in evs:
                #                 if ev.state == 0:
                #                     ev_0state = ev_0state + 1
                
                
    
    o_vertiport.users = users
    o_vertiport.eVTOLs = evtols
    vertiports['v'+str(vpt)] = o_vertiport
    output = {'vertiports':vertiports,'ene_charged':ec_SoC,'eSoC':eSoC,'unserved_users':unserved}
    return output