def oddeven(a, b, s):
    if a > b:
        return s
    s= s+a
    return oddeven(a+2, b, s)
a = int(input("Enter first number: "))
b = int(input("Enter last number: "))
s = 0
if a % 2 == 0:
    x = x
else:
    x = x+1
print("Sum is: ", oddeven(a, b, s))
if a%2 != 0:
    a = a
else:
    a = a+1
print("Sum is: ", oddeven(a, b, s))    
                  