# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 15:53:23 2018

@author: Mas
"""
# Diplomacy
class Map(object):
    
    def __init__(self):
        # Vertices
        self.NORTH = {'region' : 'NORTH', 'troop' : 'N/A', 'nation' : 'N/A'}
        self.SOUTH = {'region' : 'SOUTH', 'troop' : 'N/A', 'nation' : 'N/A'}
        # Edges
        self.NORTH_to_SOUTH = {'from' : 'NORTH', 'to' : 'SOUTH',  'troop' : 'N/A', 'action' : 'N/A', 'nation' : 'N/A'}
        self.SOUTH_to_NORTH = {'from' : 'SOUTH', 'to' : 'NORTH',  'troop' : 'N/A', 'action' : 'N/A', 'nation' : 'N/A'}
        # Limbos
        self.L_NORTH = {'region' : 'NORTH', 'troop' : 'N/A', 'nation' : 'N/A'}
        self.L_SOUTH = {'region' : 'SOUTH', 'troop' : 'N/A', 'nation' : 'N/A'}
        
    def show_map(self, M):
        print ''' '''
        print 'Map display:'
        print ''' '''
        print 'Regions display:'
        print M.NORTH 
        print M.SOUTH
        print ''' '''
        print 'Edges display (non-empty):'
        if M.NORTH_to_SOUTH['troop'] != 'N/A':
            print 'NORTH_to_SOUTH:', M.NORTH_to_SOUTH 
        else:
            pass
        if M.SOUTH_to_NORTH['troop'] != 'N/A':
            print 'NORTH_to_SOUTH:', M.SOUTH_to_NORTH         
        else:
            pass
        print ''' '''
        print 'Limbos display (non-empty):'
        if M.L_NORTH['troop'] != 'N/A':
            print 'L_NORTH:', M.L_NORTH 
        else:
            pass
        if M.L_SOUTH['troop'] != 'N/A':
            print 'L_SOUTH:', M.L_SOUTH         
        else:
            pass
        print ''' '''        
    

        
               
class Nordics(object):
    
    def __init__(self, Map):
        Map.NORTH['troop'] = 'A'
        Map.NORTH['nation'] = 'nordics'
        
                
class Teruns(object):
    
    def __init__(self, Map):
        Map.SOUTH['troop'] = 'A'
        Map.SOUTH['nation'] = 'teruns'
        
      
class Actions(object):
     
     def __init__(self):
         self.orders_display = []
     
     def hold(self, region, troop_type, current_player):
        if  region['troop'] == troop_type and region['nation'] == current_player:
            order = {'troop' : 'A', 'region' : region['region'], 'action' : 'hold'}
            orders_display.append(order)
            print 'Order from ', current_player, ':', order
            print ''' '''
        else:
            print 'Bad call'
            
     def move(self, M_move_from, M_move_to, troop_type, current_player):
        if  M_move_from['troop'] == troop_type and M_move_from['nation'] == current_player: #add valid edge check
            order = {'troop' : 'A', 'from' : M_move_from['region'], 'to' : M_move_to['region'], 'action' : 'move', 'nation' : current_player}
            orders_display.append(order)
            M.SOUTH['troop'] = 'N/A'
            M.SOUTH['nation'] = 'N/A'
            M.SOUTH_to_NORTH['troop'] = order['troop'] 
            M.SOUTH_to_NORTH['action'] = order['action']
            M.SOUTH_to_NORTH['nation'] = order['nation']
            print 'Order from ', current_player, ':', order
            print ''' '''
        else:
            print 'Bad call'
        
        


#Begin
print ''' '''
print 'Instanz Map'
M = Map()
M.show_map(M)
print 'Introducing two nations, nordics and teruns.'
nordics = Nordics(M)
teruns = Teruns(M)
M.show_map(M)
orders_display = Actions().orders_display
print 'Nordics decide to hold.' # Input
current_player = 'nordics'
troop_type = 'A'
region = M.NORTH
N_O = Actions().hold(region, troop_type, current_player)
print 'Teruns decide to move.' # Input
current_player = 'teruns'
troop_type = 'A'
M_move_from = M.SOUTH
M_move_to = M.NORTH
T_O = Actions().move(M_move_from, M_move_to, troop_type, current_player)



# fight in the NORTH
defense = 0
if M.NORTH['nation'] != 'N/A':
    defense += 1
else:
    pass
# for support in supports.....
attack = 0
if M.SOUTH_to_NORTH['nation'] != 'N/A':
    attack += 1
else:
    pass
fight = defense -attack
# for support in supports.....
if fight >= 0:
    print 'Region', M.NORTH['region'],'succesfully defended by', M.NORTH['nation'],'with troop', M.NORTH['troop'],'.'  
    M.L_SOUTH['nation'] = M.SOUTH_to_NORTH['nation']
    M.L_SOUTH['troop'] = M.SOUTH_to_NORTH['troop']
    M.SOUTH_to_NORTH['nation'] = 'N/A'
    M.SOUTH_to_NORTH['troop'] = 'N/A'
    
else:
    print 'Region', M.NORTH['region'],'conquered by', M.SOUTH_to_NORTH['nation'],'with troop', M.SOUTH_to_NORTH['troop'],'.'  
    M.L_NORTH['nation'] = M.NORTH['nation']
    M.L_NORTH['troop'] = M.NORTH['troop']    
    M.NORTH['nation'] = M.SOUTH_to_NORTH['nation']
    M.NORTH['troop'] = M.SOUTH_to_NORTH['troop']
    M.SOUTH_to_NORTH['nation'] = 'N/A'
    M.SOUTH_to_NORTH['troop'] = 'N/A'

# Fight in the SOUTH
defense = 0
if M.SOUTH['nation'] != 'N/A':
    defense += 1
else:
    pass
# for support in supports.....
attack = 0
if M.NORTH_to_SOUTH['nation'] != 'N/A':
    attack += 1
else:
    pass
fight = defense -attack  
# for support in supports.....
if fight >= 0:
    print 'Region', M.SOUTH['region'],'succesfully defended by', M.SOUTH['nation'],' with troop', M.SOUTH['troop'],'.'  
    M.L_NORTH['nation'] = M.NORTH_to_SOUTH['nation']
    M.L_NORTH['troop'] = M.NORTH_to_SOUTH['troop']
    M.NORTH_to_SOUTH['nation'] = 'N/A'
    M.NORTH_to_SOUTH['troop'] = 'N/A'
    
else:
    print 'Region', M.SOUTH['region'],'conquered by', M.NORTH_to_SOUTH['nation'],' with troop', M.NORTH_to_SOUTH['troop'],'.'  
    M.L_SOUTH['nation'] = M.SOUTH['nation']
    M.L_SOUTH['troop'] = M.SOUTH['troop']    
    M.SOUTH['nation'] = M.NORTH_to_SOUTH['nation']
    M.SOUTH['troop'] = M.NORTH_to_SOUTH['troop']
    M.NORTH_to_SOUTH['nation'] = 'N/A'
    M.NORTH_to_SOUTH['troop'] = 'N/A'

M.show_map(M)


