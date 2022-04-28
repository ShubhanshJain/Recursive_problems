''' A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a 
 number (such as 16461) that remains the same when its digits are reversed '''
 
def pal(n,t):
    if n == 0:
        return t
    else:
        t = (t*10)+(n%10)
    return pal(int(n/10),t) 
n = int(input("Enter the number: ")) 
temp = 0
p = pal(n, temp)
if (n==p):
    print(n," is a Palindrome")
else:
    print(n, "is not a palindrome")      