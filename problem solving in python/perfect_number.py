num = int(input("enter a perfect number: "))
S = 0
for i in range(1,num):
    S += i if num % i == 0 else 0
if S == num:
    print("This is a perfect number")
else:
    print("This isn't a perfect number")