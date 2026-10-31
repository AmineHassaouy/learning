# Method 1: Checking All Consecutive Sums
def isSumOfConsecutive(n):
    # Try every starting number
    for i in range(1, n):
        sum = 0
        # Generate consecutive sum
        for j in range(i, n):
            sum += j
            # If sum becomes equal to n
            # and at least two numbers are used
            if sum == n and j > i :
                return True
            # If sum exceeds n
            if sum > n:
                break
    return False

if __name__ == "__main__":

    n = 10

    if isSumOfConsecutive(n):
        print("true")
    else:
        print("false")


# Method 2: Using Power of 2 Property

def isSumOfConsecutive(n):
    
    # 1 cannot be represented
    if n == 1:
        return False

    # Check if n is power of 2
    if (n & (n - 1)) == 0:
        return False

    return True

if __name__ == "__main__":

    n = 10

    if isSumOfConsecutive(n):
        print("true")
    else:
        print("false")