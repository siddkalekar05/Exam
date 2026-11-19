import random

parent1 = [0, 1, 1, 0, 1, 0, 1, 0]
parent2 = [1, 0, 0, 1, 0, 1, 0, 1]
n = len(parent1)

def single_point_crossover(p1, p2):
    point = random.randint(1, n - 1)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2, point

def two_point_crossover(p1, p2):
    point1 = random.randint(1, n - 2)
    point2 = random.randint(point1 + 1, n - 1)
    child1 = p1[:point1] + p2[point1:point2] + p1[point2:]
    child2 = p2[:point1] + p1[point1:point2] + p2[point2:]
    return child1, child2, point1, point2

print('Production Schedule Crossover - Comparison')
print('Parent 1 :', parent1)
print('Parent 2 :', parent2)
print()
c1, c2, pt = single_point_crossover(parent1, parent2)
print('Single-Point Crossover (cut at position', pt, ')')
print(' Offspring 1 :', c1)
print(' Offspring 2 :', c2)
print()
c3, c4, pt1, pt2 = two_point_crossover(parent1, parent2)
print('Two-Point Crossover (cuts at positions', pt1, 'and', pt2, ')')
print(' Offspring 1 :', c3)
print(' Offspring 2 :', c4)
