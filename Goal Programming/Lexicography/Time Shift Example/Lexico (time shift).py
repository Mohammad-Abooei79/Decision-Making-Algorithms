import numpy  as np
from pyomo.environ import *

I = 8
# number of time periods
z2 = 280
# goal of minimum payment
z3 = 49
# goal of minimum use of staff
z4 = 0
# goal of minimum use of staff starts working by 3

M = ConcreteModel()
d = [5,7,15,21,22,12,7,3]         # minimum number of staff in each period
c = [54,57,48,42,42,42,42,45]     # payment in each time period

M.i = RangeSet(I)
M.s = RangeSet(11)

M.x = Var(M.i, within = NonNegativeIntegers)
M.sm = Var(M.s , within = NonNegativeReals)
M.sp = Var(M.s , within = NonNegativeReals)
 
M.z = Objective(expr = 1000*M.sp[1] + 1000*M.sp[2] + 1000*M.sp[3] + 1000*M.sp[4]
      + 1000*M.sp[5] + 1000*M.sp[6] + 1000*M.sp[7] + 1000*M.sp[8] + 100*M.sp[9] + 10*M.sp[10] + M.sp[11], sense = minimize)
M.ST = ConstraintList()

for i in M.x:
    if i == 8:
        M.ST.add(M.x[i] + M.x[i-7] >= d[0])
    else:
        M.ST.add(M.x[i] + M.x[i+1] >= d[i]) 

for i in M.x:
    if i == 8:
        M.ST.add(M.x[i] + M.x[i-7] + M.sm[i] - M.sp[i] == d[0])
    else:
        M.ST.add(M.x[i] + M.x[i+1] + M.sm[i] - M.sp[i] == d[i])

M.ST.add(sum(M.x[i]*c[i-1] for i in M.i) + M.sm[9] - M.sp[9] == z2) 

M.ST.add(sum(M.x[i] for i in M.i) + M.sm[10] - M.sp[10] == z3)

M.ST.add(M.x[2] + M.sm[11] - M.sp[11] == z4)                  

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
