from pyomo.environ import *

M = ConcreteModel()

M.i = RangeSet(4)
M.s = RangeSet(2)

M.x = Var(M.i, within = NonNegativeReals)
M.sm = Var(M.s , within = NonNegativeReals)
M.sp = Var(M.s , within = NonNegativeReals)

M.z = Objective(expr = (10**6)*M.sm[1] + 10*M.sm[2] , sense = minimize)

M.ST = ConstraintList()

M.ST.add(M.x[1] + M.x[3] <= 15)
M.ST.add(M.x[1] + M.x[4] <= 10)
M.ST.add(M.x[1] + M.x[2] <= 20)
M.ST.add(M.x[2] + M.x[4] <= 14)
M.ST.add(M.x[2] + M.x[3] + 2*M.x[4] <= 35)
M.ST.add(5*M.x[1] + 4*M.x[2] + M.sm[1] - M.sp[1] == 90)
M.ST.add(10*M.x[3] + 20*M.x[4] + M.sm[2] - M.sp[2] == 350)

M.pprint()
opt = SolverFactory('cplex')
results = opt.solve(M)
display(M)

print('Variables are shown below:')
for i in M.x:
    print('x[', i, '] =', M.x[i].value)
    
print('Deviations from the goals are shown below:')
for i in M.sm:
    print('d(-)', i, ' =', M.sm[i].value, '    ,   ', 'd(+)', i, '=', M.sp[i].value  )
    
print("Optimal value is shown Bellow:")
print(value(M.z))