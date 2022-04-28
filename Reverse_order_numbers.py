def Rnumber(a,b):
    if a < b:
        return
    print(a)
    return Rnumber(a-1, b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
Rnumber(a, b)