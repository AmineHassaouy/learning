def count(n):
    count = 0
    for a in range(n+1):
        for b in range(n+1):
            if a**3 + b**3 == n:
                count+=1
    return count

if __name__ == "__main__":
    print("there is", count(int(input("n = "))), "pairs that satisfies the condition a^3 + b^3 = n")