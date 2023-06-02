from pyomo.environ import *

M = ConcreteModel()

M.i = RangeSet(4)
M.j = RangeSet(1)

M.x = Var(M.i, within = NonNegativeReals)
M.y = Var(M.j , within = NonNegativeReals)

M.z = Objective(expr = M.y[1] , sense = minimize)

M.ST = ConstraintList()

M.ST.add(5*M.x[1] + 3*M.x[2] + 2*M.x[3] <= 240)
M.ST.add(3*M.x[3] + 8*M.x[4] <= 320)
M.ST.add(2*M.x[1] + 3*M.x[2] + 4*M.x[3] + 6*M.x[4] <= 180)
M.ST.add(M.y[1] + 0.0105*(10*M.x[1] + 30*M.x[2] + 50*M.x[3] + 100*M.x[4]) >= 0.0105*3000)
M.ST.add(M.y[1] + 0.8277*(M.x[1] + M.x[2]) >= 0.8277*66.67)
M.ST.add(M.y[1] + 0.1618*(M.x[1] + 4*M.x[2] + 6*M.x[3] + 2*M.x[4]) >= 0.1618*270)
         
opt = SolverFactory('cplex')
results = opt.solve(M)
display(M)

