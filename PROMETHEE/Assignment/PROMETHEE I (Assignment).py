# GitHub source Repository: <https://github.com/Valdecy/pyDecision#readme>

# !pip install pyDecision (uncomment to install packages) 

# Required Libraries
import numpy as np

from pyDecision.algorithm import promethee_i

# PROMETHEE I

# Parameters 
Q = [ 0, 2, 1, 3, 0, 0.2 ]
S = [ 0, 0, 0, 0, 0, 0 ]
P = [ 10, 3, 2, 5, 4, 0.4]
W = [0.05, 0.3, 0.3, 0.1, 0.05, 0.2]
F = ['t3', 't5', 't5', 't4', 't3', 't5'] 

''' 't1' = Usual; 't2' = U-Shape; 't3' = V-Shape; 't4' = Level; 
't5' = V-Shape with Indifference; 't6' = Gaussian; 't7' = C-Form '''

# Dataset
dataset = np.array([
        [105, 9, 5, 23, 15, 4.5],  #A1
        [110, 5, 3, 27, 19, 4.9],  #A2
        [100, 7, 1, 30, 12, 4.2],  #A3
        [120, 5, 5, 20, 20, 4.7]   #A4
        ])

# Call Promethee I
p1 = promethee_i(dataset, W = W, Q = Q, S = S, P = P, F = F, graph = True)

# Rank - Partial

#print(p1)

for i in range(0, p1.shape[0]):
  print('A'+str(i+1), p1[i])
