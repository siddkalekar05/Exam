import random

junctions = ['Hospital', 'J1', 'J2', 'J3', 'J4']
n = len(junctions)
distance = [
    [0, 3, 7, 5, 10],
    [3, 0, 4, 8, 6],
    [7, 4, 0, 2, 5],
    [5, 8, 2, 0, 3],
    [10, 6, 5, 3, 0],
]
pheromone = [[1.0] * n for _ in range(n)]
alpha, beta = 1, 2
n_ants = 5
iterations = 10
evaporation = 0.5

def route_length(route):
    return sum(distance[route[i]][route[i + 1]] for i in range(len(route) - 1))

def choose_next(current, unvisited):
    weights = []
    for j in unvisited:
        tau = pheromone[current][j] ** alpha
        eta = (1 / distance[current][j]) ** beta
        weights.append(tau * eta)
    return random.choices(unvisited, weights=weights)[0]

def build_route():
    route = [0]
    unvisited = list(range(1, n))
    current = 0
    while unvisited:
        next_node = choose_next(current, unvisited)
        route.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    route.append(0)
    return route

best_route, best_length = None, float('inf')
print('Emergency Vehicle Navigation - Pheromone-Based Route Selection')
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
print()
print('Fastest route found :', [junctions[i] for i in best_route])
print('Fastest route length :', best_length)
