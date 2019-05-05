import sys
from ast import literal_eval

def recursive_list_sum(array):

    total = 0

    for ele in array:
        if isinstance(ele, list):
            total = total + recursive_list_sum(ele)
        else:
            total = total + ele

    return total

# ATTEMPT 2
    # if len(array) == 1:
    #     return array[0]
    # else:
    #     return array[0] + rec_list_sum(array[1:])


# ATTEMPT 1
    # #base case
    # if len(lst) == 1:
    #     return lst[0]
    # else:
    #     if len(lst[0]) != 1:
    #         return rec_list_sum(lst[0])
    #     else:
    #         return lst[0] + rec_list_sum(lst[1:])



if __name__ == "__main__":
    ans = recursive_list_sum(literal_eval(sys.argv[1]))

    print(ans)
