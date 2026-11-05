from math import gcd

# Function to add two fractions
def addFraction(a, b):
    # Finding gcd of den1 and den2
    den = gcd(a[1], b[1])

    # Denominator of final fraction obtained
    # finding LCM of den1 and den2
    # LCM * GCD = a * b 
    den = (a[1] * b[1]) // den

    # Changing the fractions to have same denominator
    # Numerator of the final fraction obtained
    num = (a[0]) * (den // a[1]) + (b[0]) * (den // b[1])

    # finding the common factor of numerator and denominator
    common_factor = gcd(num, den)

    # Converting the result into simpler 
    # fraction by dividing them with common factor 
    den //= common_factor
    num //= common_factor
    return [num, den]

if __name__ == '__main__':
    a = [1, 2]
    b = [3, 2]
    ans = addFraction(a, b)
    print(f'{ans[0]}, {ans[1]}')