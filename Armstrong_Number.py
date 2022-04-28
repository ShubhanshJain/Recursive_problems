''' A number is thought of as an Armstrong number if the sum of its own digits raised to the power number of digits gives the number itself
153 = 1^3 + 5^3 +  3^3
371 = 3^3 + 7^3 + 1^3 '''

def arm(n):
    if n < 10:
        return n*n*n
    else:
        return (n%10)*(n%10)*(n%10) + arm(int(n/10))
    
n = int(input("Enter the Number: "))
r = arm(n)
if r == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not a Armstrong number")        