# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 18:24:47 2018

@author: Mas
"""

# Diplomacy

class Map(object):
    
    def __init__(self):
        # vertices
        self.NORTH = 'NORTH'
        self.SOUTH = 'SOUTH'
        # edges
        self.NORTH_to_SOUTH = []
        self.SOUTH_to_NORTH = []
        
    def show_map(self, M):
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
        Map.NORTH = 'NORTH' + '__A_nordics'
        
                
class Teruns(object):
    
    def __init__(self, Map):
        Map.SOUTH = 'NORTH' + '__A_teruns'
        
      

class Actions(object):
    
     
     def hold(object, from_, A, nation, area):
        if  area == from_ + A + nation:
            ordersdisplay = area + '__H'
            print 'Order from ', nation, ':', ordersdisplay
        else:
            print 'Bad call'
            
     def move(object, from_, to_, A, nation, area_from, mov):
        if  area_from == from_ + A + nation:
            
            ordersdisplay = A + from_ + to_
            mov.append(1)
            print 'Order from ', nation, ':', ordersdisplay
        else:
            print 'Bad call'
        




M = Map()
nordics = Nordics(M)
teruns = Teruns(M)

M.show_map(M)
from_ = 'NORTH'
A = '__A'
nation = '_nordics'

r = Actions().hold(from_, A, nation, M.SOUTH)

r = Actions().hold(from_, A, nation, M.NORTH)

to_ = '_to_SOUTH'
r = Actions().move(from_, to_, A, nation, M.NORTH, M.NORTH_to_SOUTH)

M.show_move(M)