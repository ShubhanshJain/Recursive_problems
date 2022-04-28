def pal(str):
    if (len(str) <= 1):
        return True
    if str[0] == str[len(str) - 1]:
        return pal(str[1:len(str)-1])
    else:
        return False
str = input("Enter string: ")
if pal(str):
    print(str, "is a palindrome")
else:
    print(str, "not a palindrome")        