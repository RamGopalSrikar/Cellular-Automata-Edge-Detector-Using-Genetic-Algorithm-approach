# -*- coding: utf-8 -*-
import numpy as np
import copy


def int2str(count):
    bits=9
    s="{0:b}".format(count)
    if(len(s)<bits):
        for j in range(bits-len(s)):
            s='0'+s
    return s


def mutate(C,mu):
    Cm=copy.deepcopy(C)
    count=0
    for l1 in C:
        if(np.random.uniform(0,1)<=mu):
            key=int2str(count)
            Cm[count][key]=np.random.randint(0,1)
        count=count+1
    return Cm
