"""
Comparing two algorithms to sum the first n integer numbers
"""


def uses_loop(n):
    sumit = 0
    for i in range(1, n + 1):
        sumit += i
    return sumit


def uses_formula(n):
    return n * (n + 1) / 2


# Exercise
town1 = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}
town2 = [1, 2, 3, 4, 5, 6, 7, 1]

for t1 in town1:
    print('visiting: ', f'{t1} -> {town1[t1]}')

print('visiting: ')
for i in range(len(town2)):
    arr = ' -> '
    if i == len(town2) - 1:
        arr = ''
    print(f'{town2[i]}{arr}', end='')

print('\nvisiting even number: ')
for t1 in town1:
    if t1 % 2 == 0:
        print('visiting: ', f'{t1} -> {town1[t1]}')

