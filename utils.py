#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:50:39 2021

@author: shahan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

attack_dict = {
    "Benign" :0 , 
    "Brute_Force_Web" :0 ,
    "Brute_Force_XSS" :0 ,
    "SQL_Injection" : 0
    }

Attacks = attack_dict.keys()
Nums = attack_dict.values()

def get_Count_stat(attack_dict, date):
    
    num_of_attacks = len(attack_dict)
    colors_list = ['b','g','r','c','m','y','k','w']
    colors_picked = list()
    color = list()
    
    for _ in range(num_of_attacks):
        
        if len(colors_list) == 0:
            colors_list = colors_picked
        col = random.choice(colors_list)
        color.append(col)
        colors_list.remove(col)

    
    Attacks = attack_dict.keys()
    Nums = attack_dict.values()
    print(f"{Attacks} Samples in {date} : {Nums}")
    
    fig = plt.figure(figsize = (10, 5))
     
    # creating the bar plot
    plt.bar(Attacks, Nums, color=color,
            width = 0.4)
     
    plt.xlabel("Number of Samples")
    plt.ylabel("Exploitations / Attacks")
    plt.title('Total number of Benign and Malicious samples in the dataset')
    plt.show()
    
def get_stat(data, date, fname):
    
    color = ["g","r","b","y"]
    Attacks = data["Label"].value_counts().index.to_list()
    Nums    = data["Label"].value_counts().values
    
    print(f"{Attacks} Samples in {date} : {Nums}")
    # date_3["Label"].value_counts()
    
    fig = plt.figure(figsize = (10, 5))
     
    # creating the bar plot
    plt.bar(Attacks, Nums, color=color,
            width = 0.4)
     
    plt.xlabel("Number of Samples")
    plt.ylabel("Exploitations / Attacks")
    plt.title('Total number of Benign and Malicious samples in the dataset')
    plt.savefig(f'{fname}')
    plt.show()
    print(f"Shape of {date} : {data.shape}")
    total_samples =  data.shape[0]
    return total_samples 

def get_stat_XIMB(data, date, fname):
    color = ["g","r","b","y"]
    Attacks = data["Label"].value_counts().index.to_list()
    Nums    = data["Label"].value_counts().values
    # print(type(Nums))
    Benign_ori = Nums[0]
    Benign = int(Benign_ori/2000)
    Nums[0] = Benign
    
    print(f"{Attacks} Samples in {date} : {Nums} and original Benign Samples : {Benign_ori}")
    # date_3["Label"].value_counts()
    
    fig = plt.figure(figsize = (10, 5))
     
    # creating the bar plot
    plt.bar(Attacks, Nums, color=color,
            width = 0.4)
     
    plt.xlabel("Number of Samples")
    plt.ylabel("Exploitations / Attacks")
    plt.title('Total number of Benign and Malicious samples in the dataset')
    plt.savefig(f'{fname}')
    plt.show()
    print(f"Shape of {date} : {data.shape}")
    total_samples =  data.shape[0]
    return total_samples 















