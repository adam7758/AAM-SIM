# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 02:58:17 2021

@author: zhiqiangwu
"""

class eVTOL:
    # reduce memory usage
    __slots__ = ['a_id','state','SoC','dest','users','cruise','c_state','sSoC','eSoC','cSoC','tin','tout','t_ul',
                 'taxin_hold','ssoc_cruise','esoc_cruise','csoc_cruise']
    
    speed = 150 #mph
    takeland = 2 # minutes
    battery = 140 # kWh
    capacity = 4
    reserve = 0.2 # ratio of battery capacity
    ene_charge = 0.04 # SoC
    ene_cruise = 0.01 # SoC
    ene_takeoff = 0.05 # SoC
    ene_land = 0.05 # SoC
    hover =  0.03 # SoC
    taxiout = 2 # min
    taxiin = 2 #min
    takeoff = 1 # min
    land = 1 # min
    unload = 2 # min

    
           
    def __init__(self, a_id):
        self.a_id = a_id  # id of evtol
        self.dest = 0 # no destination vertiport assigned yet.
        self.SoC = 1
        self.state = 0      #statuse of the evtol
        self.users = []
        self.cruise = 0
        self.c_state = 0 # cruise process finished
        self.sSoC = 0 # SoC when start charging
        self.eSoC = 0 # SoC when end charging
        self.cSoC = 0 # SoC charged
        self.tin = 0 # taxi-in process
        self.tout = 0 # taxi-out process     
        self.t_ul = 0 # unloading passenger process
        self.taxin_hold = 0 # 1 if evtol is in hold status after landing, 0 otherwise
        self.ssoc_cruise = 0 # soc before takeoff
        self.esoc_cruise = 0 # soc after landing
        self.csoc_cruise = 0 # soc consumed for a complete service.
        
    def add_user(self,user):
        self.users.append(user)
        
    def initialize(self): # clear user, cruise distance, cruise state when it arrives at the destination
        self.users = []
        self.cruise = 0
        self.c_state = 0
        
        
    def state_change(self):
        if self.state <= 7: # value may change
            self.state += 1
        else:
            self.state = 0
            
    def c_state_change(self):
        self.c_state += 1
    
        
class vertiport:
    # reduce memory usage
    __slots__ = ['v_id','n_cap','n_tlof','eVTOLs','users','tlof','stage']
    
    def __init__(self,v_id,n_cap,n_tlof):
        self.v_id = v_id    # vertiport id
        self.n_cap = n_cap    # number of staging pads 
        self.n_tlof = n_tlof # number of takeoff and landing pads
        self.eVTOLs = []   # evtols located at vertiport
        self.users = []   # users at the vertiport
        self.tlof = n_tlof     # number of tlof available
        self.stage = 0   # number of available staging pads


    def add_user(self,user):
        self.users.append(user)   
    def add_eVTOL(self,evtol):
        self.eVTOLs.append(evtol)    
    def remove_user(self, user):
        self.users.remove(user)    
    def remove_eVTOL(self, evtol):
        self.eVTOLs.remove(evtol)
    def add_tlof(self):
        self.tlof += 1
    def reduce_tlof(self):
        self.tlof -= 1
    def add_stage(self):
        self.stage += 1
    def reduce_stage(self):
        self.stage -= 1

        
class user:
    __slots__ = ['u_id','dest','arr_time','i_wait','s_wait','evtol','touthold','lhold','tinhold']
    
    def __init__(self,u_id,dest,arr_time):
        self.u_id = u_id
        self.dest = dest  #destination vertiport
        self.arr_time = arr_time  #acctual arrival time at vertiport
        self.i_wait = 0 # waiting time for available eVTOL
        self.s_wait = 0  #waiting time in eVTOL
        self.evtol = 0 # 0 indicating not assigned
        self.touthold = 0 # hold time for taxi out
        self.lhold = 0 # hold time for landing
        self.tinhold = 0 # hold time for taxiin
    
    def add_iwait(self):
        self.i_wait += 1
    def add_swait(self):
        self.s_wait += 1    
    def add_touthold(self):
        self.touthold += 1        
    def add_lhold(self):
        self.lhold += 1
    def add_tinhold(self):
        self.tinhold += 1 