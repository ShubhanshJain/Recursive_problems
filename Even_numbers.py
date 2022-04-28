def even(a, b):
    if a> b:
        return
    print(a)
    return even(a+2, b)
a = int(input("Enter the first Number: "))
b = int(input("Enter the second Number: "))
if a%2 == 0:
    a=a
else:
    a = a+1
even(a,b)        
    