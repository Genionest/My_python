#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-19 01:45:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pygame
from gameobjects.vector2 import *
A = (10.0,20.0)
B = (30.0,35.0)
AB = Vector2.from_points(A,B)
print("Vector AB is ",AB)
print("AB * 2 is ",AB*2)
print("AB / 2 is ",AB/2)
print("AB + (-10,5) is ",AB + (-10,5))
print("Magnitude of AB is ",AB.get_magnitude())
print("AB normalized is ",AB.get_normalized())

#结果是下面
#Vector AB is (20,15)
#AB * 2 is ( 40,30 )
#AB / 2 is ( 10,7.5 )
#AB + (-10, 5) is ( 10, 20 )
#Magnitude of AB is 25.0
#AB normalized is ( 0.8, 0.6 )