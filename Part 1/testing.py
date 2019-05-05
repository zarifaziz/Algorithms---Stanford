# Reading the file in line-by-line into a list
with open('QuickSort.txt') as f:
    lines = f.readlines()
# Removing newline characters and converting to ints
lines = [int(x.strip()) for x in lines]

print(len(lines))
