# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 18:24:47 2018

@author: Mas
"""

# Diplomacy

class Map(object):
    
    def __init__(self):
        # vertices
        self.NORTH = {'region' : 'NORTH', 'troop type' : 0, 'nation' : 'N/A'}
        self.SOUTH = {'region' : 'SOUTH', 'troop type' : 0, 'nation' : 'N/A'}
        # edges
        self.NORTH_to_SOUTH = []
        self.SOUTH_to_NORTH = []
        
    def show_map(self, M):
        print ''' '''
        print 'Map display:'
        print M.NORTH 
        print M.SOUTH
        print ''' '''
        
    def show_move(self, M):
        print 'Move display:'
        print 'NORTH_to_SOUTH:', M.NORTH_to_SOUTH 
        print 'SOUTH_to_NORTH:', M.SOUTH_to_NORTH
        print ''' '''
        

        
        
class Nordics(object):
    
    def __init__(self, Map):
        Map.NORTH['troop type'] = 'A'
        Map.NORTH['nation'] = 'nordics'
        
                
class Teruns(object):
    
    def __init__(self, Map):
        Map.SOUTH['troop type'] = 'A'
        Map.SOUTH['nation'] = 'teruns'
        
      

class Actions(object):
     
     def __init__(self):
         self.orders_display = []
     
     def hold(self, region, troop_type, current_player):
        if  region['troop type'] == troop_type and region['nation'] == current_player:
            order = {'troop' : 'A', 'region' : region['region'], 'action' : 'hold'}
            orders_display.append(order)
            print 'Order from ', current_player, ':', order
            print ''' '''
        else:
            print 'Bad call'
            
     def move(self, M_move_from, M_move_to, troop_type, current_player):
        if  M_move_from['troop type'] == troop_type and M_move_from['nation'] == current_player:
            order = {'troop' : 'A', 'from' : M_move_from['region'], 'to' : M_move_to['region'], 'action' : 'move'}
            orders_display.append(order)
            print 'Order from ', current_player, ':', order
            print ''' '''
        else:
            print 'Bad call'
        
     def orders_display(self, Map):
        pass
        

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
