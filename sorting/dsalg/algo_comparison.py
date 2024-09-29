def algo_a(n):
    sumit = 0
    for i in range(1, n + 1):
        sumit = sumit + i
    return sumit


def algo_b(n):
    sumit = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sumit = sumit + 1
    return sumit


def algo_c(n):
    return n * (n + 1) / 2


print(algo_a(5), algo_b(5), algo_c(5))

"""
Example 1: Display the first item in a list
"""


def display_first_item(data: list):
    print('first_item', data[0])


"""
Example 2: Display the first item in a list
"""


def display_all_items(data: list):
    for element in data:
        print('all_items', element)


"""
Example 3: Display all the pairs of item in a list
"""


def display_all_pairs(data: list):
    for i in data:
        for j in data:
            print(data[i], data[j])


"""
Example 4: Display all items twice in a list
"""


def display_all_items_twice(data: list):
    for e in data:
        print(e)
    for f in data:
        print(f)


sample_list = [i for i in range(10)]
display_first_item(sample_list)  # Constant time
display_all_items(sample_list)  # Linear time
display_all_pairs(sample_list)  # Quadratic time
display_all_items_twice(sample_list)  # Linear time O(2n) but the constant coefficient `2` is ignored
