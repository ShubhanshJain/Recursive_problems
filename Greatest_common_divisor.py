def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greatest common divisor is: ", gcd(a,b))