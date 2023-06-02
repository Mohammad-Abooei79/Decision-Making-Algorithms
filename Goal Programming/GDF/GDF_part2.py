# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 22:46:21 2021

@author: Mohammad_Abooei
"""

from pyomo.environ import*

M = ConcreteModel()

#parameters
I = 4
C = [2.5, 6.0, 8.0, 11.0]

#set
M.i = RangeSet(I)   

#variables
M.x = Var(M.i, within = NonNegativeReals)

#obj_func 
M.z = Objective(expr = sum(C[i-1]*M.x[i] for i in M.i) , sense = maximize )
 
#constraints
M.st = ConstraintList()

M.st.add(5*M.x[1] + 3*M.x[2] + 2*M.x[3] <= 240)
M.st.add(3*M.x[3] + 8*M.x[4] <= 320)
M.st.add(2*M.x[1] + 3*M.x[2] + 4*M.x[3] + 6*M.x[4] <= 180)

M.pprint()
solver = SolverFactory('cplex')
solver.solve(M)
display(M)

print('Variables are shown below:')
for i in M.x:
    print('x[', i, '] =', M.x[i].value)
    
print("Optimal value is shown Bellow:")
print(value(M.z))