import ahpy
import itertools

criteria_comparasion = {('Cost','Tech'):5, ('Cost','Safety'):3, ('Cost','Beauty'):7,
                        ('Tech','Safety'):1/3, ('Tech','Beauty'):5,
                        ('Safety','Beauty'):7}

criteria = ahpy.Compare('Criteria', criteria_comparasion, precision = 4)
#report = criteria.report(show = True)

tech_comparasion = {('Speed','Consumption'):3, ('Speed','Power'):2,
                    ('Consumption','Power'):2}
beauty_comparasion = {('Color','Form'):1/5}

cars = ('Mercedes', 'BMW', 'Audi')
car_pairs = list(itertools.combinations(cars, 2))
#print(car_pairs)

cost_values = (1, 1/3, 1/2)
cost_comparasion = dict(zip(car_pairs, cost_values))
#print(cost_comparasion)
speed_values = (2, 4, 3)
speed_comparasion = dict(zip(car_pairs, speed_values))
#print(speed_comparasion)
consumption_values = (1, 1/3, 1/3)
consuption_comparasion = dict(zip(car_pairs, consumption_values))

power_values = (1, 3, 2)
power_comparasion = dict(zip(car_pairs, power_values))

safety_values = (1, 1/3, 1/2)
safety_comparasion = dict(zip(car_pairs, safety_values))

color_values = (1/3, 1/2, 1/2)
color_comparasion = dict(zip(car_pairs, color_values))

form_values = (1, 3, 3)
form_comparasion = dict(zip(car_pairs, form_values))

cost = ahpy.Compare('Cost', cost_comparasion, precision=4)
tech = ahpy.Compare('Tech', tech_comparasion, precision=4)
speed = ahpy.Compare('Speed', speed_comparasion, precision=4)
consumption = ahpy.Compare('Consumption', consuption_comparasion, precision=4)
power = ahpy.Compare('Power', power_comparasion, precision=4)
safety = ahpy.Compare('Safety', safety_comparasion, precision=4)
beauty = ahpy.Compare('Beauty', beauty_comparasion, precision=4)
color = ahpy.Compare('Color', color_comparasion, precision=4)
form = ahpy.Compare('Form', form_comparasion, precision=4)

tech.add_children([speed, consumption, power])
beauty.add_children([color, form])

criteria.add_children([cost, tech,safety, beauty])

#result_tech = tech.report(show = True, verbose = True)
result = criteria.report(show = True, verbose = True)
