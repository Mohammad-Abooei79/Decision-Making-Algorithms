from pyomo.environ import *


M = ConcreteModel()

M.i = RangeSet(4)

M.x = Var(M.i, within = NonNegativeReals)

M.z = Objective(expr = 1.542*(1-exp(-0.0055*(5*M.x[1] + 4*M.x[2]))) + 0.661*(1-exp(-0.0036*(10*M.x[3] + 20*M.x[4]))) 
                 - 0.355*(1-exp(-0.0055*(5*M.x[1] + 4*M.x[2])))*(1-exp(-0.0036*(10*M.x[3] + 20*M.x[4]))), sense = maximize)

M.ST = ConstraintList()

M.ST.add(M.x[1] + M.x[3] <= 15)
M.ST.add(M.x[1] + M.x[4] <= 10)
M.ST.add(M.x[1] + M.x[2] <= 20)
M.ST.add(M.x[2] + M.x[4] <= 14)
M.ST.add(M.x[2] + M.x[3] + 2*M.x[4] <= 35)

M.pprint()
opt = SolverFactory('ipopt')
results = opt.solve(M)
display(M)

print('Variables are shown below:')
for i in M.x:
    print('x[', i, '] =', M.x[i].value)
    
print("Optimal value is shown Bellow:")
print(value(M.z))