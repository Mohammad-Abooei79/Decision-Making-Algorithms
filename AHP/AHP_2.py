#import ahpy
from ahpy import *

cost_comparasion = {('A','B'):1/3, ('A','C'):1/4, ('B','C'):1/2}
fuel_comparasion = {('A','B'):1/4, ('A','C'):1/6, ('B','C'):1/3}
comfort_comparasion = {('A','B'):2, ('A','C'):8, ('B','C'):6}
model_comparasion = {('A','B'):1/3, ('A','C'):4, ('B','C'):7}

criteria_comparasion = {('Cost','Fuel'):3, ('Cost','Comfort'):2, ('Cost','Model'):2,
                        ('Fuel','Comfort'):1/4, ('Fuel','Model'):1/4,
                        ('Comfort','Model'):1/2}

cost = ahpy.Compare(name='Cost', comparisons=cost_comparasion, precision=4, random_index='saaty')
fuel = ahpy.Compare(name='Fuel', comparisons=fuel_comparasion, precision=4, random_index='saaty')
comfort = ahpy.Compare(name='Comfort', comparisons=comfort_comparasion, precision=4, random_index='saaty')
model = ahpy.Compare(name='Model', comparisons=model_comparasion, precision=4, random_index='saaty')
criteria = ahpy.Compare('Criteria', criteria_comparasion, precision=4, random_index='saaty')

criteria.add_children([cost, fuel, comfort, model])

#print(criteria.target_weights)

report = criteria.report(show=True)
#print(report)
