import random

routes = ['Route-A', 'Route-B', 'Route-C', 'Route-D', 'Route-E']
distances = [12, 7, 15, 9, 11]
fitness_values = [1 / d for d in distances]

def roulette_wheel_selection():
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    running_total = 0
    for i in range(len(routes)):
        running_total += fitness_values[i]
        if running_total >= pick:
            return routes[i]
    return routes[-1]

def tournament_selection(k=3):
    contenders = random.sample(range(len(routes)), k)
    best_index = max(contenders, key=lambda i: fitness_values[i])
    return routes[best_index]

print('Delivery Route Planning - Parent Selection Strategies')
print('Routes    :', routes)
print('Distances :', distances)
print()
print('Roulette Wheel Selection results:')
for _ in range(5):
    print(' Selected parent ->', roulette_wheel_selection())
print()
print('Tournament Selection results:')
for _ in range(5):
    print(' Selected parent ->', tournament_selection())
