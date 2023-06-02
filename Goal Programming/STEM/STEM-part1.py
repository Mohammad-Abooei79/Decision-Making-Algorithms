from pyomo.environ import *

M = ConcreteModel()

M.i = RangeSet(4)

M.x = Var(M.i, within = NonNegativeReals)

M.z1 = Objective(expr = 10*M.x[1] + 30*M.x[2] + 50*M.x[3] + 100*M.x[4] , sense = maximize)
#M.z2 = Objective(expr = M.x[1] + M.x[2] , sense = maximize)
#M.z3 = Objective(expr = M.x[1] + 4*M.x[2] + 6*M.x[3] + 2*M.x[4] , sense =  maximize)

M.ST = ConstraintList()

M.ST.add(5*M.x[1] + 3*M.x[2] + 2*M.x[3] <= 240)
M.ST.add(3*M.x[3] + 8*M.x[4] <= 320)
M.ST.add(2*M.x[1] + 3*M.x[2] + 4*M.x[3] + 6*M.x[4] <= 180)

opt = SolverFactory('cplex')
results = opt.solve(M)
display(M)