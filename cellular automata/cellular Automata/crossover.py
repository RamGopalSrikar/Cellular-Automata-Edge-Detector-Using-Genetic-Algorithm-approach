# -*- coding: utf-8 -*-

import numpy as np
import copy
import FitnessEval as fit
import mutate
def crossover(p1,p2,mu,crossover_rate):
    c1=copy.deepcopy(p1)
    c2=copy.deepcopy(p2)
   
    
#    alpha=0.3
    
    count=0
    for l1,l2 in zip(p1,p2):
        if(np.random.uniform(0,1)<=crossover_rate):
            c1[count]=l2
            c2[count]=l1
        count=count+1
        
    c1m=mutate.mutate(c1,mu)
    c2m=mutate.mutate(c2,mu) 
    return c1m,c2m


 