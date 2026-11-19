import random

target = (5, 5)
n_particles = 4
iterations = 8
parameter_sets = [
    {'name': 'High Inertia (More Exploration)', 'w': 0.9, 'c1': 1.2, 'c2': 1.2},
    {'name': 'Low Inertia (Faster Convergence)', 'w': 0.4, 'c1': 1.5, 'c2': 1.5},
    {'name': 'Balanced Setting', 'w': 0.6, 'c1': 1.5, 'c2': 1.5},
]

def distance(pos):
    return ((pos[0] - target[0]) ** 2 + (pos[1] - target[1]) ** 2) ** 0.5

def run_pso(w, c1, c2):
    positions = [[random.uniform(0, 10), random.uniform(0, 10)] for _ in range(n_particles)]
    velocities = [[0, 0] for _ in range(n_particles)]
    personal_best = [p[:] for p in positions]
    global_best = min(personal_best, key=distance)
    for _ in range(iterations):
        for i in range(n_particles):
            r1, r2 = random.random(), random.random()
            for d in range(2):
                velocities[i][d] = (w * velocities[i][d]
                    + c1 * r1 * (personal_best[i][d] - positions[i][d])
                    + c2 * r2 * (global_best[d] - positions[i][d]))
                positions[i][d] += velocities[i][d]
            if distance(positions[i]) < distance(personal_best[i]):
                personal_best[i] = positions[i][:]
        global_best = min(personal_best, key=distance)
    return distance(global_best)

print('Impact of PSO Parameters on Robot Navigation Efficiency')
print()
for params in parameter_sets:
    final_distance = run_pso(params['w'], params['c1'], params['c2'])
    print(params['name'], '-> w =', params['w'], ', c1 =', params['c1'],
          ', c2 =', params['c2'], ', Final distance to target =', round(final_distance, 3))
