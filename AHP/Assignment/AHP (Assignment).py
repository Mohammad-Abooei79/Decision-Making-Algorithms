import ahpy
import itertools

criteria_comparasion = {('Cost','Speed'):3, ('Cost','Consumption'):2, ('Cost','Power'):5, ('Cost','Weight'):9,
                        ('Speed','Consumption'):1/2, ('Speed','Power'):3, ('Speed','Weight'):6,
                        ('Consumption','Power'):3, ('Consumption','Weight'):5,
                        ('Power','Weight'):4}

criteria = ahpy.Compare('Criteria', criteria_comparasion, precision = 4)
#report = criteria.report(show = True)

cars = ('Mercedes', 'BMW', 'Audi', 'McLaren')
car_pairs = list(itertools.combinations(cars, 2))
#print(car_pairs)

cost_values = (1, 1/3, 3, 1/3, 3, 5 )
cost_comparasion = dict(zip(car_pairs, cost_values))
#print(cost_comparasion)
speed_values = (2, 5, 1/3, 3, 1/5, 1/7)
speed_comparasion = dict(zip(car_pairs, speed_values))
#print(speed_comparasion)
consumption_values = (1, 1/3, 3, 1/3, 3, 5)
consuption_comparasion = dict(zip(car_pairs, consumption_values))

power_values = (1, 5, 1/3, 5, 1/3, 1/5)
power_comparasion = dict(zip(car_pairs, power_values))

weight_values = (1, 1/2, 1, 1/2, 1, 3)
weight_comparasion = dict(zip(car_pairs, weight_values))

cost = ahpy.Compare('Cost', cost_comparasion, precision=4)
speed = ahpy.Compare('Speed', speed_comparasion, precision=4)
consumption = ahpy.Compare('Consumption', consuption_comparasion, precision=4)
power = ahpy.Compare('Power', power_comparasion, precision=4)
weight = ahpy.Compare('Weight', weight_comparasion, precision=4)

criteria.add_children([cost, speed,consumption, power, weight])

#result_tech = tech.report(show = True, verbose = True)
result = criteria.report(show = True, verbose = True)
