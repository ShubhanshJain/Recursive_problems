def series(a, b):
    if a>b:
        return 0
    print(a*a)
    return series(a+1, b)
a = int(input("Enter first number: "))
b = int(input("Enter last number: "))
print("Series is: ")
series(a,b)