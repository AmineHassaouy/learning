# this program reads a date then returns the date of the next day, it test if it's a leap year and if it's a 30 or 31 days month and if it's february
d = int(input("enter the day: "))
m = int(input("enter the month: "))
y = int(input("enter the year: "))

leap = None
days = None

# determining the year
if y%400 == 0:
    leap = True
elif y%100 ==0:
    leap = False
elif y%4 == 0:
    leap = True
else:
    leap = False

# determining the month
if m in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif m in [4, 6, 9, 11]:
    days = 30
elif m == 2:
    days = 29 if leap else 28
else:
    print("Invalid Month")
    exit()

# incrementing the day
if d < days:
    d += 1
elif d == days:
    d = 1
    if m ==12:
        m = 1
        y += 1
    else:
        m += 1
else: 
    print("invalid day")
    exit()
print(f"The next day is: {d:02d}/{m:02d}/{y}")