# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:01:51 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def  plantTree(x,y,z):
    mc.setBlocks(x,y,z,x,y+4,z,18)
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,17)
    
x,y,z = mc.player.getTilePos()
for i in range(10):
    for j in range(5):
        for k in range(5):
            plantTree(x+i*5,y+j*5,z+k*5)
        
    
        
