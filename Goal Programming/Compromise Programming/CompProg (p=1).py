# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 02:21:19 2022

@author: Asus
"""

from pyomo.environ import *

M = ConcreteModel()

z1 = 90
z2 = 350
M.i = RangeSet(4)

M.x = Var(M.i, within = NonNegativeReals)

M.Z = Objective(expr = (5*M.x[1] + 4*M.x[2] - z1)/z1 + (10*M.x[3] + 20*M.x[4] - z2)/z2 , sense = maximize)

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

print("Optimal value is shown Bellow:")
print(value(M.Z))