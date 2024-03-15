from time import time
def compute_average(n):
    data = []
    start = time()
    n = input("n: ")
    n = int(n)
    squares = [k*k for k in range(1, n+1)]

    squares = []
    for k in range(1, n+1):
        squares.append(k*k)
    
    end = time()
    return (end - start)/n

print("Average time per operation = {}".format(compute_average(10)))
