# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 00:04:21 2021

@author: Mohammad_Abooei
"""

from pyomo.environ import*

M = ConcreteModel()

#parameters
I = 4
Phi = [0.279, 0.021, -0.487, 0.187]
Phi_2 = [0.046, -0.179, 0.212, -0.079] #For Sensitivity Analysis
Distance = [150, 180, 80, 200]
Allowed = 200

#set
M.i = RangeSet(I)   

#variables
M.x = Var(M.i, within = Binary)

#obj_func  (if you want to perform SA, uncomment Phi_2 and the second M.obj) 
M.obj = Objective(expr = sum(Phi[i-1]*M.x[i] for i in M.i) , sense = maximize )

#M.obj = Objective(expr = sum(Phi_2[i-1]*M.x[i] for i in M.i) , sense = maximize ) #for SA
 
#constraints
M.st = ConstraintList()

M.st.add(M.x[1] + M.x[2] + M.x[4] <= 1)
M.st.add(sum(Distance[i-1]*M.x[i] for i in M.i) <= Allowed)

M.pprint()
opt = SolverFactory('cplex')
results = opt.solve(M)
display(M)
