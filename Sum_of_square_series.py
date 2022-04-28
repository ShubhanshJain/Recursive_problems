def sum(a,b):
    if a> b:
        return 0
    return a*a + sum(a+1, b)
a = int(input("Enter first number: "))
b = int(input("Enter last number: "))
print("Sum of given series is: ", sum(a,b))