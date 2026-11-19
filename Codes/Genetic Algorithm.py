import random

jobs = [5, 8, 3, 9, 4, 7, 6, 2]
n_jobs = len(jobs)
pop_size = 6
generations = 20
mutation_rate = 0.1

def create_chromosome():
    return [random.randint(0, 1) for _ in range(n_jobs)]

def fitness(chromosome):
    machine1 = sum(jobs[i] for i in range(n_jobs) if chromosome[i] == 0)
    machine2 = sum(jobs[i] for i in range(n_jobs) if chromosome[i] == 1)
    difference = abs(machine1 - machine2)
    return 100 - difference

def tournament_selection(population):
    contenders = random.sample(population, 3)
    contenders.sort(key=fitness, reverse=True)
    return contenders[0]

def crossover(parent1, parent2):
    point = random.randint(1, n_jobs - 1)
    return parent1[:point] + parent2[point:]

def mutate(chromosome):
    for i in range(n_jobs):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

population = [create_chromosome() for _ in range(pop_size)]
for gen in range(generations):
    new_population = []
    for _ in range(pop_size):
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child = mutate(crossover(parent1, parent2))
        new_population.append(child)
    population = new_population

best = max(population, key=fitness)
print('Production Scheduling using Genetic Algorithm')
print('Jobs (processing times):', jobs)
print('Best schedule found     :', best)
print('Best fitness            :', fitness(best))
