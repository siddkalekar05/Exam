import random

# Small dataset: six binary features and a class label (0 or 1)
dataset = [
    ([1, 0, 1, 1, 0, 1], 1),
    ([0, 1, 0, 0, 1, 0], 0),
    ([1, 1, 1, 0, 0, 1], 1),
    ([0, 0, 1, 0, 1, 0], 0),
    ([1, 0, 1, 1, 1, 1], 1),
    ([0, 1, 0, 1, 0, 0], 0),
    ([1, 1, 0, 1, 1, 1], 1),
    ([0, 0, 0, 0, 1, 0], 0),
]
n_features = 6
pop_size = 6
generations = 15
mutation_rate = 0.1

def predict(features, chromosome):
    selected_values = [features[i] for i in range(n_features) if chromosome[i] == 1]
    if len(selected_values) == 0:
        return 0
    return 1 if sum(selected_values) >= (len(selected_values) / 2) else 0

def fitness(chromosome):
    correct = 0
    for features, label in dataset:
        if predict(features, chromosome) == label:
            correct += 1
    accuracy = correct / len(dataset)
    penalty = sum(chromosome) * 0.01
    return accuracy - penalty

def create_chromosome():
    return [random.randint(0, 1) for _ in range(n_features)]

def tournament_selection(population):
    contenders = random.sample(population, 3)
    contenders.sort(key=fitness, reverse=True)
    return contenders[0]

def crossover(p1, p2):
    point = random.randint(1, n_features - 1)
    return p1[:point] + p2[point:]

def mutate(chromosome):
    for i in range(n_features):
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
accuracy = sum(1 for features, label in dataset if predict(features, best) == label) / len(dataset)
print('GA-Based Feature Selection for Improving Model Performance')
print('Best feature subset (1 = selected) :', best)
print('Number of features selected        :', sum(best))
print('Accuracy with this subset          :', accuracy)
