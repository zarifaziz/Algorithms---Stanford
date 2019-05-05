import sys

"""
Compute the number of inversions in a text file
"""
def merge_count_split_inv(arr_1, arr_2):
    # finding total length of output array
    total_length = len(arr_1) + len(arr_2)
    # initialising
    arr_output = []
    count = 0
    i = 0
    j = 0

    for k in range(total_length):
        # The first array is exhausted
        if i == len(arr_1):
            arr_output.append(arr_2[j])
            j += 1
        # The second array is exhausted
        elif j == len(arr_2):
            arr_output.append(arr_1[i])
            i += 1
        # First array value is smaller
        elif arr_1[i] < arr_2[j]:
            arr_output.append(arr_1[i])
            i += 1
        # Right array value is smaller
        else:
            arr_output.append(arr_2[j])
            j += 1
            count = count + len(arr_1) - i
#         print('i: ', i)
#         print('j: ', j)
    return (count, arr_output)



def count_inversions(array):

    count = 0
    arr_length = len(array)
    # Base case
    if arr_length == 1: return (0,array)

    # X, Y and Z are the sorted arrays
    else:
        left_inv_count, X = count_inversions(array[0:arr_length//2])
        right_inv_count, Y  = count_inversions(array[arr_length//2:arr_length])
        split_inv_count, Z = merge_count_split_inv(X, Y)

    # totalling the counts
    count = left_inv_count + right_inv_count + split_inv_count

    return (count, Z)


# Reading the file in line-by-line into a list
with open('IntegerArray.txt') as f:
    lines = f.readlines()
# Removing newline characters and converting to ints
lines = [int(x.strip()) for x in lines]

count, sorted_array = count_inversions(lines)

print(count)
