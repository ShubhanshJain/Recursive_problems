def natural(a, b):
    if a > b:
        return
    print(a)
    return natural(a+1, b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
natural(a, b)