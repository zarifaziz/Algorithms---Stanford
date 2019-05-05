import sys

def hello(a,b):
    print("Hello and this is your sum: ",a + b)

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    hello(a,b)
