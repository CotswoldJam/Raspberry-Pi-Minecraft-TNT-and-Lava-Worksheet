#!/usr/bin/env python3
# (C) Steve Martin, 2019

from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
mc.setBlock(x+3, y+3, z, block.LAVA.id)
sleep(20)
mc.setBlock(x+3, y+5, z, block.WATER.id)
sleep(4)
mc.setBlock(x+3, y+5, z, block.AIR.id)
