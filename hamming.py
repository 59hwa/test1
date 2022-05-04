#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:01:55 2022

@author: sejinpark
"""

 
import matplotlib.pyplot as plt
import math
import numpy as np
 
hamming = np.zeros((11))
 
for i in range(11):
    hamming[i] = math.pow(math.sin(math.pi*i/10),2)
   
plt.plot(hamming)

plt.show()