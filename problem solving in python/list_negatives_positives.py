L = []
n = None
while n == None:
    n = int(input("Enter the dimension of the list (don't pass 50): ")) 
    if n > 50 or n <= 0:
        print("This dimension isn't supported by the program, Try again.")
        n = None
        continue
    for i in range(n):
        L.append(int(input(f"Enter L[{i+1}] = ")))
    print(L)

    positives = 0
    negatives = 0
    
    for nombre in L:
        if nombre > 0:
            positives += 1
        elif nombre < 0:
            negatives += 1
            
    print(f"There are {positives} positive numbers, and {negatives} negative numbers")