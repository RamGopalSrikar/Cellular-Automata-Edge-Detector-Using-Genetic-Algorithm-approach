# -*- coding: utf-8 -*-
import copy
import numpy as np

def int2bin(im):
    image=copy.deepcopy(im)
    w,h=image.shape
    for x_pixel in range(w):
        for y_pixel in range(h):
            if image[x_pixel][y_pixel]>128:
                image[x_pixel][y_pixel]=1
            else:
                image[x_pixel][y_pixel]=0
    return image

def bin2int(im):
    image=copy.deepcopy(im)
    w,h=image.shape
    for x_pixel in range(w):
        for y_pixel in range(h):
            if image[x_pixel][y_pixel]==1:
                image[x_pixel][y_pixel]=255
            else:
                image[x_pixel][y_pixel]=0
    return image
def str_rep(sub):
    s=''
    for i in sub:
        for j in i:
            s=s+str(j)
    
    return s 

def get_rule(sub,ind_table):
    for i in ind_table:
        if(sub in i):
            rule=i[sub]
    return rule


def final_image(ind_table,start_image):
    start_image_bin=int2bin(start_image)
    final_image=copy.deepcopy(start_image_bin)
    l=len(start_image)
   
    for i in range(l):
        for j in range(l):
            if(i+3<=l): 
                if(j+3<=l):
                     sub=copy.deepcopy(start_image_bin[i:i+3,j:j+3])
                else:
                    k=len(start_image_bin[j:l])
                    sub=np.append(start_image_bin[i:i+3,j:l],start_image_bin[i:i+3,0:3-k],axis=1)
            else: 
                if(j+3<=l):
                    k1=len(start_image_bin[i:l])
                    
                    sub=np.append(start_image_bin[i:l,j:j+3],start_image_bin[0:3-k1,j:j+3],axis=0)
                else:
                    k=len(start_image_bin[j:l])
                    k1=len(start_image_bin[i:l])
                    sub1=start_image_bin[i:l,j:l]
                    sub2=start_image_bin[i:l,0:3-k]
                    sub12=np.append(sub1,sub2,axis=1)
                    sub3=np.append(start_image_bin[0:3-k1,3-k:3],start_image_bin[0:3-k1,0:3-k],axis=1)
                    sub=np.append(sub12,sub3,axis=0)
                    
            sub_key=str_rep(sub)
            rule=get_rule(sub_key,ind_table)
            if(rule==1):
                val=1
            elif(rule==0):
                val=0
        
            if(i+1<l):
                if(j+1<l):
                    final_image[i+1,j+1]=val
                else:
                    final_image[i+1,l-j-1]=val
            else:
                if(j+1<l):
                    final_image[l-i-1,j+1]=val
                else:
                    final_image[l-i-1,l-j-1]=val
    
    final=bin2int(final_image)                
    return final
            
                



                
                 
           
    
    
    
    
    
    
    

    

    

    
    