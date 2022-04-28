def evensum(a, b, s):
    if a>b:
        return s
    s = s+a
    print(a)
    return evensum(a+2, b, s)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
s = 0
if a%2 == 0:
    a = a
else:
    a = a+1
print("Sum of given even numbers are: ", evensum(a, b, s))        