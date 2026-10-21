# write a program that calculates the sum of N first terms 
# of the harmonic series 1+ 1/2 + 1/3 + ... + 1/N
n = int(input("N = "))
series = 0
for i in range(1, n+1):
    series += 1/i
print(f'the sum of the {n} first terms of the harmonic series is: ', series)
