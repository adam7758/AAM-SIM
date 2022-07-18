# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 03:14:58 2021

@author: zhiqiangwu
"""

from Inputs import los1,los2

def ev_update(vpt,vertiports):
    new_users = [] # served users
    ec_SoC = []
    eSoC = []
    ec_soc_cruise = []
    o_vertiport = vertiports['v'+str(vpt)]
    # check and update status of evtol
    evtols = o_vertiport.eVTOLs
    elec_usage = 0
    for e in evtols:       
        
        # update evtol at state 0, ready state
        if e.state == 0:
            continue
               
        ## update evtol at state 1, loading passengers
        # check capacity
        elif e.state == 1:
            if len(e.users) >= e.capacity or e.users[0].s_wait >= los1 or e.users[-1].s_wait >= los2:
                # if there is available tolf
                if o_vertiport.tlof > 0:
                                    
                    e.state_change()
                    o_vertiport.reduce_tlof()
                    o_vertiport.add_stage()
                else:
                    for u in e.users:
                        u.add_touthold()
            else:
                for u in e.users:
                    u.add_swait()  
        
        
        ## update evtol at state 2, taxi-out
        elif e.state == 2:
            if e.tout >= e.taxiout:
                e.state_change()
                e.tout = 0
                e.ssoc_cruise = e.SoC
            else:
                e.tout += 1
                
                
        ## update evtol at state 3, takeoff
        elif e.state == 3:
            e.state_change()
            e.SoC = e.SoC - e.ene_takeoff
            o_vertiport.add_tlof()
        
        
        ## update evtol at state 4, cruise
        elif e.state == 4:
            # Destination vertiport of evtol
            d_vertiport = vertiports['v'+str(e.dest)]
            
            if e.c_state < e.cruise: # if evtol is still in cruise
                e.c_state_change()
                e.SoC = e.SoC - e.ene_cruise
            else: # if evtol finished cruise, 3 conditions needs to be satisfied.
                if (e.SoC <= e.reserve and
                    d_vertiport.tlof >= 1) or d_vertiport.tlof >=2 or (d_vertiport.tlof >=1 and d_vertiport.stage >= 1):                                                                                                                   
                    e.state_change()
                    d_vertiport.reduce_tlof()
                else:
                    e.SoC = e.SoC - e.hover
                    for u in e.users:
                        u.add_lhold()
                        
            vertiports['v'+str(e.dest)] = d_vertiport
        
        ## update evtol at state 5, landing
        elif e.state == 5:
            # Destination vertiport of evtol
            d_vertiport = vertiports['v'+str(e.dest)]

            if e.taxin_hold == 0: # if taxi in process is not hold
                e.SoC = e.SoC - e.ene_land
                e.taxin_hold = 1
                e.sSoC = e.SoC
                e.esoc_cruise = e.SoC
                e.csoc_cruise = e.esoc_cruise - e.ssoc_cruise
                ec_soc_cruise.append(e.csoc_cruise)
                
            if d_vertiport.stage > 0:
                e.state_change()
                d_vertiport.reduce_stage()
                d_vertiport.add_tlof()
                e.taxin_hold = 0
            else:
                
                for u in e.users:
                    u.add_tinhold()
                    
            vertiports['v'+str(e.dest)] = d_vertiport
                
        ## update evtol at state 6,taxi-in
        elif e.state == 6:
            # Destination vertiport of evtol
            d_vertiport = vertiports['v'+str(e.dest)]
            if e.tin >= e.taxiin:
                new_users = new_users + e.users 
                e.initialize()
                e.tin = 0
                e.state_change()
                e.dest = 0
                    
                o_vertiport.remove_eVTOL(e)    
                d_vertiport.add_eVTOL(e)                
                vertiports['v'+str(e.dest)] = d_vertiport
                
            else:
                e.tin = e.tin +1
                      
        ## update evtol at state 7,unloading passengers
        elif e.state == 7:
            if e.t_ul >= e.unload:
                e.state_change()
                e.t_ul = 0
            else:
                e.t_ul = e.t_ul +1
               
       ## update evtol at state 8, charging state
        elif e.state == 8:
            elec_usage = elec_usage + e.ene_charge*e.battery
            if e.SoC <= 1:
                e.SoC = e.SoC + e.ene_charge
            else:
                e.SoC = 1
                e.eSoC = e.SoC
                e.cSoC = e.eSoC - e.sSoC
                ec_SoC.append(e.cSoC)
                eSoC.append(e.eSoC)
                e.state_change()   
                
    
    vertiports['v'+str(vpt)] = o_vertiport    
    output = {'vertiports':vertiports,'elec_usage':elec_usage,'served_users':new_users,'ene_charged':ec_SoC,'eSoC':eSoC,'ene_consumed':ec_soc_cruise}
    return output