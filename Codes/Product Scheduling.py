import random

def objective(v):
    x, y = v
    return x ** 2 + y ** 2

bounds = (-10, 10)
pop_size = 6
iterations = 15

def run_ga():
    population = [[random.uniform(*bounds), random.uniform(*bounds)] for _ in range(pop_size)]
    for _ in range(iterations):
        population.sort(key=objective)
        parents = population[:3]
        children = []
        while len(children) < pop_size:
            p1, p2 = random.sample(parents, 2)
            child = [(p1[d] + p2[d]) / 2 + random.uniform(-0.5, 0.5) for d in range(2)]
            children.append(child)
        population = children
    return min(population, key=objective)

def run_pso():
    w, c1, c2 = 0.6, 1.5, 1.5
    positions = [[random.uniform(*bounds), random.uniform(*bounds)] for _ in range(pop_size)]
    velocities = [[0, 0] for _ in range(pop_size)]
    personal_best = [p[:] for p in positions]
    global_best = min(personal_best, key=objective)
    for _ in range(iterations):
        for i in range(pop_size):
            r1, r2 = random.random(), random.random()
            for d in range(2):
                velocities[i][d] = (w * velocities[i][d]
                    + c1 * r1 * (personal_best[i][d] - positions[i][d])
                    + c2 * r2 * (global_best[d] - positions[i][d]))
                positions[i][d] += velocities[i][d]
            if objective(positions[i]) < objective(personal_best[i]):
                personal_best[i] = positions[i][:]
        global_best = min(personal_best, key=objective)
    return global_best

def run_de():
    F, CR = 0.5, 0.7
    population = [[random.uniform(*bounds), random.uniform(*bounds)] for _ in range(pop_size)]
    for _ in range(iterations):
        new_population = []
        for i in range(pop_size):
            candidates = [population[j] for j in range(pop_size) if j != i]
            a, b, c = random.sample(candidates, 3)
            mutant = [a[d] + F * (b[d] - c[d]) for d in range(2)]
            trial = [mutant[d] if random.random() < CR else population[i][d] for d in range(2)]
            if objective(trial) < objective(population[i]):
                new_population.append(trial)
            else:
                new_population.append(population[i])
        population = new_population
    return min(population, key=objective)

ga_best = run_ga()
pso_best = run_pso()
de_best = run_de()
print('Comparing GA, PSO and DE for Production Scheduling Optimization')
print()
print('Genetic Algorithm          -> Best =', [round(v, 3) for v in ga_best], ', Fitness =', round(objective(ga_best), 4))
print('Particle Swarm Optimization -> Best =', [round(v, 3) for v in pso_best], ', Fitness =', round(objective(pso_best), 4))
print('Differential Evolution      -> Best =', [round(v, 3) for v in de_best], ', Fitness =', round(objective(de_best), 4))
