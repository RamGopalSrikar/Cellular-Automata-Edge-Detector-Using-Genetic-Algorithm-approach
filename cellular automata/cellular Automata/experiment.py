# -*- coding: utf-8 -*-
import cv2
import initialize_population as ipop
import json
import numpy as np
import FitnessEval as fit
import final_image1 as fi
import matplotlib.pyplot as plt


initial_image = cv2.imread("binaryhand.png", 0)
    
ipop.initialize_population(initial_image, 2, bonus = True)

with open("CellularAutomata.json",'r') as f:
  population = json.loads(f.read());

with open("solution.json",'r') as f:
  table = json.loads(f.read());

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
   
f=fi.final_image(table,start_image)
fitness=fit.calculate_fitness(init_image,f)

print(' fitness:{}'.format(fitness))
plt.imshow(f,cmap='gray')
plt.show()


