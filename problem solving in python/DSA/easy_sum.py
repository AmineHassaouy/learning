# Method 1: normal way
def findSum(n):
    sum = 0
    i = 1
    
    # Iterating over all the numbers between 1 to n
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum
    
if __name__ == "__main__":
    n = 5
    print(findSum(n))
    
# Method 2: best approach
def findSum(n):
    
    # Using mathematical formula to compute
    # sum of first n natural numbers
    return n * (n + 1) // 2
    
if __name__ == "__main__":
    n = 5
    print(findSum(n))