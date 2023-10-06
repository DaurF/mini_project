import sys

def add(x, y): return x + y

def sub(x, y): return x - y

if __name__ == '__main__':
    x, y = int(sys.argv[1]), int(sys.argv[2])
    print(x, y)
    print(add(x, y))
    print(sub(x, y))
