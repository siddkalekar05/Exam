import random

target = (5, 5)
n_particles = 4
iterations = 6
w, c1, c2 = 0.5, 1.5, 1.5

def distance(pos):
    return ((pos[0] - target[0]) ** 2 + (pos[1] - target[1]) ** 2) ** 0.5

positions = [[random.uniform(0, 10), random.uniform(0, 10)] for _ in range(n_particles)]
velocities = [[0, 0] for _ in range(n_particles)]
personal_best = [p[:] for p in positions]
global_best = min(personal_best, key=distance)

print('Warehouse Robot Path Optimization using PSO')
print('Target location:', target)
print()
for it in range(iterations):
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
    print('Iteration', it + 1, ': Best position =', [round(v, 2) for v in global_best],
          ', Distance to target =', round(distance(global_best), 2))
