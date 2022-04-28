def hailstrone(num,a):
    if num == 1:
        a.append(num)
        return a
    print(num, end=" ")
    if num % 2 == 0:
        return hailstone((int(num/2)), a)
    else:
        return hailstone(num*3 + 1, a)
num = int(input("enter any number: "))
a = []   
print(hailstone(num,a))
 