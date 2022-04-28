def count(n):
    if n < 10:
        return 1
    else:
        return 1 + count(int(n/10))
    
n = int(input("Enter the number: "))
print("Total number of digits are: ", count(n))    