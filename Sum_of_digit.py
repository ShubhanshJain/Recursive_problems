def sum(n):
    if n < 10:
        return n
    else:
        return (n%10) + sum(int(n/10))
    
n = int(input("Enter the number: "))
print("Sum of Digit is: ", sum(n))    