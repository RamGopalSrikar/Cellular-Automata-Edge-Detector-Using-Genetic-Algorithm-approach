# -*- coding: utf-8 -*-
import numpy as np
import copy
def exponential_ranking(pop_gen,npop,fitness):
    sort_cdf=list(sorted(set(fitness),reverse=True))
    
    C=npop-((np.exp(-npop)-1)/(np.exp(-1)-1))
    ranking=[0 for i in range(0,npop)]
    prob=[0 for i in range(0,npop)]
    count=0
    for i in range(len(sort_cdf)):
        for j in range(npop):
            if(sort_cdf[i]==fitness[j]):
                ranking[j]=count
                count=count+1
    
    for m in range(npop):
        if(m>0):
            prob[m]=prob[m-1]+(1-np.exp(-ranking[m]))/C
        else:
            prob[m]=(1-np.exp(-ranking[m]))/C
            m=m+1
                     
    m=np.random.uniform(0,1)
    n=np.random.uniform(0,1)
    for i in range(npop):
        if m<=prob[i]:
            p1=pop_gen[i+2]
            break
    for j in range(npop):    
        if n<=prob[j]:
            p2=pop_gen[j+2]
            break
    return p1,p2  

def tournament_sel(pop_gen,npop,k,fitness):
    q1=np.random.permutation(npop)
    q2=np.random.permutation(npop)
    p1_arr=q1[0:k]
    p2_arr=q2[0:k]
    best_costp1=10000000
    best_costp2=10000000
    for i in range(k):
        val=p1_arr[i]+2
        val2=p2_arr[i]+2
        if fitness[val-2]<best_costp1:
            temp_p1=pop_gen[val]
            best_costp1=fitness[val-2]
        if fitness[val2-2]<best_costp2:
            temp_p2=pop_gen[val2]
            best_costp2=fitness[val2-2]
    
    p1=copy.deepcopy(temp_p1)
    p2=copy.deepcopy(temp_p2)
    return p1,p2
   