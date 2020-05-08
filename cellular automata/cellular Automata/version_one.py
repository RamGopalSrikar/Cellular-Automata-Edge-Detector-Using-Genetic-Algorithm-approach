# -*- coding: utf-8 -*-

import copy
import parent_selection as ps
import crossover as cr
import final_image as fi
import FitnessEval as fit
import numpy as np
import matplotlib.pyplot as plt

def version_one(initial_image,npop,gen,population,fitness_list,mu,crossover_rate,final_image_list):
    
    pop_gen=copy.deepcopy(population)
    temp=dict()
    high_fitness=min(fitness_list)
    fitness_c=copy.deepcopy(fitness_list)
    bestsolution=copy.deepcopy(final_image_list[0])
    avg_fit=[]
    high_fit=[]
    org_gen=copy.deepcopy(gen)
    start_image = np.asarray(population[0])
    best_table=copy.deepcopy(population[2])
    
    while(gen>0):
        
        gen=gen-1
        popc=[]
        fitc=[]
        
        
        
          
        for j in range(npop//2):
            #parent selection
#            p1,p2=ps.exponential_ranking(pop_gen,npop,fitness_c)
            p1,p2= ps.tournament_sel(pop_gen,npop,20,fitness_c)
            #child generation
            c1,c2=cr.crossover(p1,p2,mu,crossover_rate)
            
            final1=fi.final_image(c1,start_image)
            fitn1=fit.calculate_fitness(initial_image,final1)
    
            final2=fi.final_image(c2,start_image)
            fitn2=fit.calculate_fitness(initial_image,final2)
            
            if(fitn1<high_fitness):
                bestsolution=copy.deepcopy(final1)
                high_fitness=fitn1
                best_table=copy.deepcopy(c1)
                
            if(fitn2<high_fitness):
                bestsolution=copy.deepcopy(final2)
                high_fitness=fitn2
                best_table=copy.deepcopy(c2)
            
            popc.append(copy.deepcopy(c1))
            popc.append(copy.deepcopy(c2))
            fitc.append(fitn1)
            fitc.append(fitn2)
            
            pop_gen.append(copy.deepcopy(c1))
            pop_gen.append(copy.deepcopy(c2))
            fitness_c.append(fitn1)
            fitness_c.append(fitn2)
            
            
        
        fit_ordered=sorted(fitness_c)
        
        
        temp=[]
        temp.append(pop_gen[0])
        temp.append(pop_gen[1])
        count=0;
        for l1 in fit_ordered:
            for i in range(len(fitness_c)):
                if(fitness_c[i]==l1):
                    temp.append(pop_gen[i+2])
                    count=count+1;
                    if(count>=npop):
                        break
            
                
        pop_gen=copy.deepcopy(temp)
        fitness_c=copy.deepcopy(fit_ordered[0:npop])
        avg_fitness=0
        
        for item in fitness_c:
            avg_fitness=avg_fitness+item
        
        avg_fit.append(avg_fitness/npop)
        high_fit.append(fitness_c[0])
       
        print('gen {}: fitness:{}'.format(org_gen-gen,fitness_c[0]))
        plt.imshow(bestsolution,cmap='gray')
        plt.show()
        
#    print('after running GA algorithm')
#    display(pop_gen[str(0)],passes)
    return high_fit,avg_fit,best_table
            
