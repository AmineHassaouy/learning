# determine if an integer is a prime number
x = int(input("x = "))
if x<2:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            is_prime = False
            break

    print("Prime" if is_prime else "Not Prime")