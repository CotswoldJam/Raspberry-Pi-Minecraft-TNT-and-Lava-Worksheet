#!/usr/bin/env python3
# (C) Steve Martin, 2019

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
print("You are at:", x, y, z)
