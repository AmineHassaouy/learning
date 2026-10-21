# write a program to calculate the n-th term Un of fibonacci sequence 
# given by: U1 = 1, U2 = 1, Un = Un-1 + Un-2 for n > 2
u = [1, 1]
n = int(input("n = "))
for i in range(2, n):
    u.append(u[(i-1)] + u[(i-2)]) 
print(f"U(n) = {u[n-1]}" if n>0 else "Invalid n")