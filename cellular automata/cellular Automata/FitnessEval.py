# -*- coding: utf-8 -*-
import cv2

def calculate_fitness(start_image, final_image):
  edges = cv2.Canny(start_image, 256, 256)
#  edges=goal_image
  fitness = 0
  w,h=edges.shape
  for x_pixel in range(w):
    for y_pixel in range(h):
      if final_image[x_pixel][y_pixel] != edges[x_pixel][y_pixel]:
        fitness = fitness + 1

  return fitness