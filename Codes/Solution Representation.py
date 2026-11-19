import random

items = ['ItemA', 'ItemB', 'ItemC', 'ItemD', 'ItemE']
max_quantity = 10

binary_solution = [random.randint(0, 1) for _ in items]
integer_solution = [random.randint(0, max_quantity) for _ in items]
permutation_solution = items.copy()
random.shuffle(permutation_solution)

print('Warehouse Inventory - Solution Representations')
print('Items:', items)
print()
print('Binary representation      :', binary_solution)
print('Integer representation     :', integer_solution)
print('Permutation representation :', permutation_solution)

target_stock = 30
total_allocated = sum(integer_solution)
fitness = abs(target_stock - total_allocated)
print()
print('Total allocated quantity :', total_allocated)
print('Fitness (distance from target, lower is better) :', fitness)
