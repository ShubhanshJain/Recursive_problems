def odd(a, b):
    if a> b:
        return
    print(a)
    return odd (a+2, b)
a = int(input("Enter first number: "))
b = int(input("Enter last number: "))
if a % 2 != 0:
    a = a
else:
    a = a+1
odd(a,b)            