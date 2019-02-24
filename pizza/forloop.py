import numpy as np
from reader import *

'''
For an integer max_size, returns tuples of all possible integers a, b where a < b and a * b = max_size.
'''
def all_perms(max_size):
    result = []
    if max_size == 2:
        return [(1, 2)]
    for i in range(1, int(np.sqrt(max_size)) + 1):
        if max_size % i == 0:
            result.append((i, max_size // i))
    return result

'''
Takes sum of the rectangle ((i, j), (i+m, j+n)) in matrix mat.
'''
def sum_cells(i, j, m, n, mat):
    total = 0
    for i in range(i, i + m):
        for j in range(j, j + n):
            total += mat[i][j]
    return total

'''
Solves the pizza problem recursively.
'''
def solve(R, C, L, H, pizza, used):
    max_size = 2 * H
    num_slices = 0
    output = []
    while True:
        perms = all_perms(max_size)
        for perm in perms:
            if perm[0] <= R and perm[1] <= C:
                for i in range(R - perm[0] + 1):
                    for j in range(C - perm[1] + 1):
                        if not sum_cells(i, j, perm[0], perm[1], used):
                            mushroom = sum_cells(i, j, m, n, pizza)
                            if mushroom >= L and max_size - mushroom >= L:
                                for k in range(i, i + perm[0]):
                                    for l in range(j, j + perm[1]):
                                        used[k][l] = 1
                                num_slices += 1
                                output.append((i, j, i + perm[0], j + perm[1]))
                                break
                            # continue
            if perm[1] <= R and perm[0] <= C:
                for i in range(R - perm[1] + 1):
                    for j in range(C - perm[0] + 1):
                        if not sum_cells(i, j, perm[1], perm[0], used):
                            mushroom = sum_cells(i, j, m, n, pizza)
                            if mushroom >= L and max_size - mushroom >= L:
                                for k in range(i, i + perm[1]):
                                    for l in range(j, j + perm[0]):
                                        used[k][l] = 1
                                num_slices += 1
                                output.append((i, j, i + perm[1], j + perm[0]))
                                break
                            # continue
        if sum([sum(r) for r in used]) == R * C:
            break
        max_size -= 1
    return (num_slices, output)
                        
R, C, L, H, pizza, used = read("a_example.in")
print(solve(R, C, L, H, pizza, used)[0])