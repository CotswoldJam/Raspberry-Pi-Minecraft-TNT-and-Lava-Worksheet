#!/usr/bin/env python3
# (C) Steve Martin, 2019

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
mc.setBlocks(x+3, y, z, x+7, y+4, z+4, block.TNT.id, 1)
