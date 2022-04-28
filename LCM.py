def lcm(a, b, c):
    c = c+b
    if c%a ==0 and c%b ==0:
        return c
    return lcm(a, b, c)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = 0
print("LCM = ", lcm(a,b,c))