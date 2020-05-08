# -*- coding: utf-8 -*-

import cv2
import initialize_population as ipop
import json
import numpy as np
import FitnessEval as fit
import final_image as fi
import matplotlib.pyplot as plt
import version_one as one
import statistics as st
import random

npop=50
gen=50
mu=0.1
crossover_rate=0.4
runs=2



best_fitness1=[]
avg_fitness1=[]
mean_bestfit1=[]
stddev_bestfit1=[]
mean_avgfit1=[]
stddev_avgfit1=[] 

def visualize_image(filename,image):
  cv2.imwrite(filename,image)   
  
def print_population(population_json):
    json_obj = json.loads(population_json)
    for individual in range(len(population)):
        print(population[individual])


for run in range(runs):
    print(run)
    random.seed(100*(3+run))
    final_image_list=[]
    fitness_list=[]
    initial_image = cv2.imread("binaryhand.png", 0)
    
    ipop.initialize_population(initial_image, npop, bonus = False)
    
    with open("CellularAutomata.json",'r') as f:
      population = json.loads(f.read());
    
    start_image = np.asarray(population[0])
    goal_image = np.asarray(population[1])
    
    
    init_image=start_image.astype(np.uint8)
    print('fitness:{}'.format(fit.calculate_fitness(init_image,goal_image)))
    print('start image')
    plt.imshow(start_image,cmap='gray')
    plt.show()
    print('goal image')
    plt.imshow(goal_image,cmap='gray')
    plt.show()
    
    for i in range(npop):
        f=fi.final_image(population[i+2],start_image)
        fitness=fit.calculate_fitness(init_image,f)
        final_image_list.append(f)
        fitness_list.append(fitness)
        
    
    
    high_fit,avg_fit,table=one.version_one(init_image,npop,gen,population,fitness_list,mu,crossover_rate,final_image_list)
    best_fitness1.append(high_fit)
    avg_fitness1.append(avg_fit)
    with open("solution.json",'w') as o:
        o.write(json.dumps(table))


for i in range(0,gen):
    x1=np.asarray(best_fitness1)
    y1=np.asarray(avg_fitness1)
    mean_bestfit1.append(st.mean(x1[:,i]))
    stddev_bestfit1.append(st.stdev(x1[:,i]))
    
    mean_avgfit1.append(st.mean(y1[:,i]))
    stddev_avgfit1.append(st.stdev(y1[:,i]))
    


plt.plot(mean_bestfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('mean')
plt.title('(GA) 1 versions mean of maximum fitness')
plt.grid(True)
plt.legend()
plt.show()     

plt.plot(stddev_bestfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('standered deviation')
plt.title('(GA) 1 versions  standered deviation of maximum  fitness')
plt.grid(True)
plt.legend()
plt.show()  

plt.plot(mean_avgfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('mean')
plt.title('(GA) 1 versions  mean of average fitness')
plt.grid(True)
plt.legend()
plt.show()     

plt.plot(stddev_avgfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('standered deviation')
plt.title('(GA) 1 versions standered deviations of average fitness')
plt.grid(True)
plt.legend()

