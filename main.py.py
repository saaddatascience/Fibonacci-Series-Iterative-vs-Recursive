import time 

def fibonacciIterative(n):
    previousNum = 0
    currentNumber = 1
    for i in range(1,n):
        previouspreviousNumber = previousNum
        previousNum = currentNumber
        currentNumber = previouspreviousNumber + previousNum
    return currentNumber

    
def fiborecursive(n):
    if n ==0:
        return 0
    elif(n==1):
        return 1 
    else:
        return fiborecursive(n-1) + fiborecursive(n-2)
    


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    init = time.time()
    print(f"by using iterative func value of fib{num} is {fibonacciIterative(num)}")
    print(f"by using recursion func value of fib{num} is {fiborecursive(num)}")
    print(f"it took {time.time() - init} seconds")
    