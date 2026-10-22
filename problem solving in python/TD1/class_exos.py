# import math
# xa, ya = int(input("Entrer xa")), int(input("Entrer ya"))
# xb, yb = int(input("Entrer xb")), int(input("Entrer yb"))
# DIST = math.sqrt((xa-xb)**2+(ya-yb)**2)
# print(DIST)



# ex2
# print("***Method 1***")
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = int(input("d = "))
# sum = a + b + c + d
# print("Sum = ", sum)

# print("***Method 2***")
# sum = 0
# for i in range(4):
#     x = int(input(f"x({i}) = "))
#     sum += x
# print('Sum = ', sum)

# ex3
# anne = -1
# while anne <= 0:
#     anne = int(input("Entrer une anne: "))
#     if anne <=0:
#         continue

#     if anne % 400 == 0 :
#         print("bisextile")
#     elif anne % 100 == 0:
#         print("normale")
#     elif anne % 4 == 0:
#         print("bisextile")
#     else:
#         print("normale")
# # method2
# anne = int(input("entrer une anne: "))
# est_bisextile = (anne % 400 ==0 and anne%100 != 0) or (anne % 4 ==0)
# print("bisextile: ", est_bisextile)


# ex4
# n = -1
# series = 0
# while n <= 0:
#     n = int(input("N = "))
#     if n <= 0:
#         continue

#     for i in range(1, n+1):
#         series += 1/i
# print(f'la somme du premiers nombres est: ', series)