# write a program that takes X (flaot) as input 
# and calculates the numerical value of a polynomial of degree n
# p(X) = AnX^n + AnX^n-1 + ... + A1X + 0
# n, An coefficients, X are entered by the user
n = int(input("Enter the degree of the polynomial: n = "))
A = []
for i in range(n+1):
    A.append(float(input(f"A{i} = ")))
x = int(input('X = '))

p = 0
for i in range(n+1):
    p += A[i]*x**i
print('P(x) = ', p)