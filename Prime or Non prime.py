def prime(num, i):
    if (i == 1):
        return 1
    if (num % i) == 0: # returns remainder
        return 0
    return prime(num, i -1)

num = int(input("Enter any number: "))
n = prime(num, int(num/2)) # returns quotient
if n == 1:
    print("Number is Prime")
else:
    print("non - prime")    