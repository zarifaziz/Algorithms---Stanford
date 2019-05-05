import sys

"""
Assignment 1 - Implementing karatsuba's algorithm
- for some reason, wasn't getting the correct answer when multiplying
- 64 digit numbers
"""

def karatsuba(x,y):

	# Base case: if one of the numbers become single digits, multiply
	# normally
	if (x/10 < 10) or (y/10 < 10):
		return x*y

	# if not, split the numbers up into smaller fragments and multiply
	# get the length of the largest number
	n = max(len(str(x)),len(str(y)))
	m = n - n//2

	# Splitting the number into smaller parts
	A  = x // 10**m
	B = x % 10**m
	C = y // 10**m
	D = y % 10**m

	z_0 = karatsuba(B,D)
	z_2 = karatsuba(A,C)
	z_1 = karatsuba(A+B, C+D) - z_2 - z_0

	# final product call
	product = z_2*10**n + z_1*10**m + z_0

	return product

if __name__ == "__main__":
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	answer = karatsuba(x,y)
	print(answer)

# x = 3141592653589793238462643383279502884197169399375105820974944592
# y = 2718281828459045235360287471352662497757247093699959574966967627
#
# 8 539 734 222 673 567 065 463 550 869 546 574 495 034 888 535 765 114 961 879 601 127 067 743 044 893 204 848 617 875 072 216 249 073 013 374 895 871 952 806 582 723 184
#
# 8 539 734 222 673 567 065 463 550 869 546 574 495 034 888 535 654 238 035 06 812 462 706 774 304 489 320 484 861 787 507 221 624 907 301 337 489 587 195 280 658 272 3184

# from online
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

# print(karatsuba(x,y))
