#!/usr/bin/env python3
# (C) Steve Martin, 2019

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
mc.setBlock(x+3, y, z, block.TNT.id, 1)
