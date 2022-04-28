def des(n):
    if n ==0 or n == 1:
        print(n, end = " ")
        return
    des (int(n/2))
    des(n%2)
n = int(input("Enter the decimal number: "))
print("binary equivalent is: ")
des(n)    
        