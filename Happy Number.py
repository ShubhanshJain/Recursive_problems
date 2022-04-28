def sumdigit(num):
    if num == 0:
        return 0
    return ((num%10)*(num%10) + sumdigit(num//10))
def happy(num):
    if num == 1:
        return True
    if num == 4:
        return False
    return happy(sumdigit(num))

num = int(input("Enter any number: "))
if happy(num):
    print("Number is happy")
else:
    print("Number is unhappy")    