# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 11:47:12 2023

@author: hamza
"""

import numpy as np 

"""n is the population at t0 
modelling the growth of a population 
g number of generation(iterations) 
l is lumbda for poisson         """
def populationgrowth(n,g,l):
    rng = np.random.default_rng()
    
    for i in range (g):
        m= rng.poisson(lam=l, size=n)
        n=np.sum(m)
         if n>0:
            l=l*50/n
        print(n)
populationgrowth(10, 10, 2)        
