# GitHub source Repository: <https://github.com/Valdecy/pyDecision#readme>

# !pip install pyDecision (uncomment to install packages) 

# Required Libraries
import numpy as np

from pyDecision.algorithm import promethee_ii

# PROMETHEE II

# Parameters 
Q = [ 0, 2, 1, 3, 0, 0.2 ]
S = [ 0, 0, 0, 0, 0, 0 ]
P = [ 10, 3, 2, 5, 4, 0.4]
W = [0.05, 0.3, 0.3, 0.1, 0.05, 0.2]
F = ['t3', 't5', 't5', 't4', 't3', 't5'] 

# 't1' = Usual; 't2' = U-Shape; 't3' = V-Shape; 't4' = Level; 't5' = V-Shape with Indifference; 't6' = Gaussian; 't7' = C-Form

# Dataset
dataset = np.array([
        [105, 9, 5, 23, 15, 4.5],  #A1
        [110, 5, 3, 27, 19, 4.9],  #A2
        [100, 7, 1, 30, 12, 4.2],  #A3
        [120, 5, 5, 20, 20, 4.7]   #A4
        ]) 

#Sensitivity_Analysis (change the dataset to perform SA)
''' dataset = np.array([
        [105, 9, 5, 23, 15, 4.5],  #A1
        [110, 5, 3, 27, 19, 4.9],  #A2
        [100, 7, 7, 30, 12, 4.5],  #A3
        [120, 5, 5, 20, 20, 4.7]   #A4
        ]) '''  

# Call Promethee II
p2 = promethee_ii(dataset, W = W, Q = Q, S = S, P = P, F = F, sort = True, topn = 10, graph = True)

# Rank
#print(p2)

for i in range(0, p2.shape[0]):
  print('A'+str(p2[i,0])+': '+str(round(p2[i,1],3)))