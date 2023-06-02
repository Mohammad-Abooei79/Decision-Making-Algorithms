# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 20:41:59 2022

@author: Asus
"""

from pyomo.environ import *

M = ConcreteModel()

Beta = 10**(-4)
#print(Beta)
#r1 = 90
r2 = 350
#eps1 = 54
eps2 = 210 

M.i = RangeSet(4)

M.x = Var(M.i, within = NonNegativeReals)
M.s2 = Var(within = NonNegativeReals)

M.Z = Objective(expr = 5*M.x[1] + 4*M.x[2] + Beta*((M.s2/r2)) , sense = maximize)

M.ST = ConstraintList()

M.ST.add(10*M.x[3] + 20*M.x[4] - M.s2 == eps2)
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