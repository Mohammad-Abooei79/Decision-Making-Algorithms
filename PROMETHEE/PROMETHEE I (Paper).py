# GitHub source Repository: <https://github.com/Valdecy/pyDecision#readme>

# !pip install pyDecision (uncomment to install packages) 

# Required Libraries
import numpy as np

from pyDecision.algorithm import promethee_i

# PROMETHEE I

# Parameters 
Q = [ 50, 100000, 10, 165, 1, 1, 1 ]
S = [ 50, 100000, 10, 165, 1, 1, 1 ]
P = [ 50, 100000, 10, 165, 1, 1, 1 ]
W = [0.05, 0.25, 0.15, 0.25, 0.15, 0.1, 0.05]
F = ['t6', 't6', 't6', 't6', 't2', 't2', 't2'] 

''' 't1' = Usual; 't2' = U-Shape; 't3' = V-Shape; 't4' = Level; 
't5' = V-Shape with Indifference; 't6' = Gaussian; 't7' = C-Form '''

# Dataset
dataset = np.array([
        [-25, 10018735, 39, 625, 2, 2, 1],  #Istanbul  a1
        [-60, 3370866, 21, 138, 2, 1, 1],   #Izmir     a2
        [-60, 4007860, 13, 383, 2, 1, 1],   #Ankara    a3
        [-182, 2125140, 27, 9, 2, 1, 1 ],   #Bursa     a4
        [-480, 1206085, 15, 121, 2, 2, 1]   #Kocaeli   a5
        ])

# Call Promethee I
p1 = promethee_i(dataset, W = W, Q = Q, S = S, P = P, F = F, graph = True)

# Rank - Partial

#print(p1)

for i in range(0, p1.shape[0]):
  print('A'+str(i+1), p1[i])
