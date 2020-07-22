# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:34:41 2020

@author: user
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mport Minecraft

while True:
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x,y-1,z+i,41)
    