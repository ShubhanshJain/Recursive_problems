def lserch(n, item,s):
    if s < 0:
        return -1
    if n[s] == item:
        return s
    return lserch(n, item, s-1)
n = []
for i in range(6):
    i = int(input("Enter numbers in pocket ["+str(i)+"]"))
    n.append(i)
print(n)
item = int(input("Enter number to serch: "))
index = lserch(n, item, 5)
if index == -1:
    print("Not Found")
else:
    print("Found inn index ", index)        