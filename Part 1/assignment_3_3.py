import sys

"""
Assignment 3 - Implementing the QuickSort algorithm
- for some reason, wasn't getting the correct answer when multiplying
- 64 digit numbers
"""

def choosePivot(array):
    m = len(array)

    a = array[0]
    # if the length is even, choose middle manually
    if m % 2 == 0:
        b = array[(m//2)-1]
    else:
        b = array[m//2]

    c = array[-1]

    if a <= b <= c or c <= b <= a:
        return array.index(b), b
    elif b <= a <= c or c <= a <= b:
        return 0, a
    else:
        return -1, c



def QuickSort(array):

    # m is the lenth of the subarray, return if length is 1 or 0
    m = len(array)
    if m == 1 or m == 0 : return (array, 0)

    init_count = m - 1

    p_index, pivot = choosePivot(array)

    # exchange pivot element with first element
    array[p_index], array[0] = array[0], array[p_index]

    # PARTITION SUBROUTINE
    i = 1
    for j in range(1,m):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    # swapping the pivot into the right place
    array[0], array[i-1] = array[i-1], array[0]

    # Recursively sort the left and right side of the array
    array[0:i-1], left_count = QuickSort(array[0:i-1])
    array[i:j+1], right_count = QuickSort(array[i:j+1])

    count = left_count + right_count + init_count

    return array, count

# Reading the file in line-by-line into a list
with open('QuickSort.txt') as f:
    lines = f.readlines()
# Removing newline characters and converting to ints
lines = [int(x.strip()) for x in lines]

sorted_array, count = QuickSort(lines)

print(count)
