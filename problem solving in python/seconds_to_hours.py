# this program converts an integer, expected to be in seconds, to "hours, minutes, seconds"
num = int(input("enter a number in seconds"))
H = num//3600
M = (num%3600) // 60
S = num % 60