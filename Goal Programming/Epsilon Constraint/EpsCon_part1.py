# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 17:09:29 2022

@author: Mohammad_Abooei
"""
from pyomo.environ import *

M = ConcreteModel()

M.i = RangeSet(4)

M.x = Var(M.i, within = NonNegativeReals)

#M.z1 = Objective(expr = 5*M.x[1] + 4*M.x[2] , sense = maximize) 
M.z2 = Objective(expr = 10*M.x[3] + 20*M.x[4] , sense = maximize) 

'''uncomment the objective function to find its optimal value''' 

M.ST = ConstraintList()

M.ST.add(M.x[1] + M.x[3] <= 15)
M.ST.add(M.x[1] + M.x[4] <= 10)
M.ST.add(M.x[1] + M.x[2] <= 20)
M.ST.add(M.x[2] + M.x[4] <= 14)
M.ST.add(M.x[2] + M.x[3] + 2*M.x[4] <= 35)

M.pprint()
opt = SolverFactory('cplex')
results = opt.solve(M)
display(M)

print('Variables are shown below:')
for i in M.x:
    print('x[', i, '] =', M.x[i].value)
