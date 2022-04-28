def rev(str, l):
    if l > 0:
        print(str[l], end = '')
        return rev(str, l-1)
    if l ==0:
        print(str[0])
str = input("Enter any string: ")        
print("Reverse of string: ", rev(str, len(str)-1) )