# Given two positive numbers x and y, check if y is a power of x or not.
def is_power_m1(x, y):
    if x == 1:
        return y == 1
    
    k = 1
    while k < y:
        k *= x
    
    return y == k

def is_power_m2(x, y):
    if x == 1: 
        return y == 1
    
    if y == 1:
        return True
    
    rem = y
    while rem % x ==0:
        rem //= x
    return rem == 1

if __name__ == "__main__":
    print("This algorithm only supports positive integers.")
    x, y = int(input("x = ")), int(input("y = "))
    print("** Method 1 **: ", f"{y} is a power of {x}" if is_power_m1(x, y) else f"{y} is not a power of {x}")
    print("** Method 2 **: ", f"{y} is a power of {x}" if is_power_m2(x, y) else f"{y} is not a power of {x}")