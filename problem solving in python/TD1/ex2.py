# write a program to calculate the sum of 4 numbers
# these 4 numbers are integers
# the first method should use 5 variables
# and the second should use 2 variables
print("***Method 1***")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
sum = a + b + c + d
print("Sum = ", sum)

print("***Method 2***")
sum = 0
for i in range(4):
    x = int(input(f"x({i}) = "))
    sum += x
print('Sum = ', sum)