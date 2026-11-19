import random

locations = ['Warehouse', 'A', 'B', 'C', 'D']
n = len(locations)
distance = [
    [0, 4, 8, 6, 12],
    [4, 0, 5, 9, 7],
    [8, 5, 0, 3, 6],
    [6, 9, 3, 0, 4],
    [12, 7, 6, 4, 0],
]
pheromone = [[1.0] * n for _ in range(n)]
n_ants = 5
iterations = 10
evaporation = 0.5

def route_length(route):
    return sum(distance[route[i]][route[i + 1]] for i in range(len(route) - 1))

def build_route():
    route = [0]
    unvisited = list(range(1, n))
    current = 0
    while unvisited:
        weights = [pheromone[current][j] / distance[current][j] for j in unvisited]
        next_node = random.choices(unvisited, weights=weights)[0]
        route.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    route.append(0)
    return route

best_route, best_length = None, float('inf')
print('Delivery Route Optimization using Ant Colony Optimization')
for it in range(iterations):
    routes = [build_route() for _ in range(n_ants)]
    lengths = [route_length(r) for r in routes]
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - evaporation)
    for route, length in zip(routes, lengths):
        for i in range(len(route) - 1):
            a, b = route[i], route[i + 1]
            pheromone[a][b] += 1 / length
            pheromone[b][a] += 1 / length
    iteration_best = min(lengths)
    if iteration_best < best_length:
        best_length = iteration_best
        best_route = routes[lengths.index(iteration_best)]
    print('Iteration', it + 1, ': best length this iteration =', iteration_best)
print()
print('Best route found :', [locations[i] for i in best_route])
print('Best route length :', best_length)
