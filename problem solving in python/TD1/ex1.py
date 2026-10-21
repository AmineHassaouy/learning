# write a program to calculate and show the distance (float) 
# between two points A and B 
# with coordinates (xa, ya) (xb, yb) are entered as integers
import math
xa, ya = int(input("Enter Xa: ")), int(input("Enter Ya: "))
xb, yb = int(input("Enter Xb: ")), int(input("Enter Yb: "))
DIST = math.sqrt((xb-xa)**2+(yb-ya)**2)
print("The distance between these two points is: ", DIST)