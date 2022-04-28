def power(a, b):
    if b == 1:
        return a
    else:
        return a*power(a, b-1)
    
num = int(input("Enter the Number: "))
n = int(input("Enter power value: "))
print("Power value: ", power(num, n))    