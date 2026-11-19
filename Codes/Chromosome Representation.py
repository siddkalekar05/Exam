import random

employees = ['Aman', 'Bhavna', 'Chetan', 'Divya', 'Esha']
shifts = [0, 1, 2]  # 0 = Morning, 1 = Afternoon, 2 = Night
preferred_shift = [0, 1, 2, 0, 1]

def create_chromosome():
    return [random.choice(shifts) for _ in employees]

def create_population(pop_size):
    return [create_chromosome() for _ in range(pop_size)]

def fitness(chromosome):
    score = 0
    for i in range(len(chromosome)):
        if chromosome[i] == preferred_shift[i]:
            score += 1
    return score

population = create_population(5)
print('Employee Shift Scheduling - Population and Fitness')
print('Preferred shifts:', preferred_shift)
print()
for index, chromosome in enumerate(population):
    print('Chromosome', index + 1, ':', chromosome, '-> Fitness =', fitness(chromosome))
