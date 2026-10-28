# Method 1: Loop 
def gcd(a, b):
    
    # Everything divides 0
    if(a==0 or b==0):
        return max(a, b)
        
    # Find Minimum of a and b
    result = min(a, b)

    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    # Return gcd of a and b
    return result


if __name__ == '__main__':
    a = 20
    b = 28
    print(gcd(a, b))

# Method 2: Euclidean Algorithm using Subtraction
def gcd(a, b):
  
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Base case
    if a == b:
        return a

    # a is greater
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)

if __name__ == '__main__':
    a = 20
    b = 28
    print(gcd(a, b))

# Method 3: Euclidean Algorithm using Subtraction by Checking Divisibility
def gcd(a, b):
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Base case
    if a == b:
        return a

    # a is greater
    if a > b:
        if a % b == 0:
            return b
        return gcd(a - b, b)

    # b is greater
    if b % a == 0:
        return a
    return gcd(a, b - a)


if __name__ == '__main__':
    a = 20
    b = 28
    print(gcd(a, b))

# Method 4: Optimized Euclidean Algorithm by Checking Remainder

# Recursive function to calculate GCD using Euclidean algorithm
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

if __name__ == '__main__':
    a = 20
    b = 28
    print(gcd(a, b))

# Method 5: Built-in Function
import math

def gcd(a, b):
    return math.gcd(a, b)


if __name__ == '__main__':
    a = 20
    b = 28
    print(gcd(a, b))