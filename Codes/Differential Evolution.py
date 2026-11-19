import random

def objective(vector):
    x, y = vector
    return x ** 2 + y ** 2


pop_size = 6
generations = 15
F = 0.5
CR = 0.7
bounds = (-10, 10)
population = [[random.uniform(*bounds), random.uniform(*bounds)] for _ in range(pop_size)]
print('Engineering Design Optimization using Differential Evolution')
for gen in range(generations):
    new_population = []
    for i in range(pop_size):
        candidates = [population[j] for j in range(pop_size) if j != i]
        a, b, c = random.sample(candidates, 3)
        mutant = [a[d] + F * (b[d] - c[d]) for d in range(2)]
        trial = []
        for d in range(2):
            if random.random() < CR:
                trial.append(mutant[d])
            else:
                trial.append(population[i][d])
        if objective(trial) < objective(population[i]):
            new_population.append(trial)
        else:
            new_population.append(population[i])
    population = new_population
    best = min(population, key=objective)
    print('Generation', gen + 1, ': Best design =', [round(v, 3) for v in best],
          ', Cost =', round(objective(best), 4))
