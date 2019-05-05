import copy
import math
import sys
import random


# Reading the file in line-by-line into a list
with open('kargerMinCut.txt') as f:
    lines = f.readlines()
G = {}
for line in lines:
    lst = [int(s) for s in line.split()]
    G[lst[0]] = lst[1:]

def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

# Karger minimum cut Algorithm
def karger(G):
    length = []
    while len(G) > 2:
        # Picking an edge uniformly at random
        v1, v2 = choose_random_key(G)
        # Combining the edges of v2 into v1
        G[v1].extend(G[v2])
        # Replacing v2's edges with v1's edges
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        # deleting self loops
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    return length[0]

def operation(n):
    i = 0
    count = 10000
    while i < n:
        data = copy.deepcopy(G)
        min_cut = karger(data)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count

print(operation(100))
