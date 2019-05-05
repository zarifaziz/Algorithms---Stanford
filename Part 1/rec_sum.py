import sys

def rec_sum(lst):

    #Base case
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[-1] + rec_sum(lst[:-1])


if __name__ == "__main__":
    string = sys.argv[1]
    digits = [int(i) for i in str(string)]
    answer = rec_sum(digits)
    print(answer)
