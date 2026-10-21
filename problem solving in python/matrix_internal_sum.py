M = []
L, C = None, None
while L == None or C == None:
    L = int(input('Enter the number of lines: '))
    C = int(input('Enter the number of columns: '))
    if L > 50 or C > 50 or L <= 0 or C <= 0:
        L, C = None, None
        print("This dimension isn't supported, Try again.")
        continue

    for i in range(L):
        print(f"Line {i}: ")
        M.append([])
        for j in range(C):
            M[i].append(int(input(f"Enter the element M[{i}][{j}] = ")))

    for i in range(L):
        for j in range(C):
            print(M[i][j], end=" ")
        print()
    
    S = 0
    for i in range(L):
        for j in range(C):
            S += M[i][j]
    print('The sum of each line and column is: ', S)