def bserch(arr, item):
    beg = 0
    last = len(arr)-1
    while (beg<=last):
        mid = int((beg+last)/2)
        if (item == arr[mid]):
            return mid
        if (item > arr[mid]):
            beg = mid+1
        else:
            last = mid_1
    else:
        return False        
n = int(input("Enter size of Array: "))
print("Enter values in Ascending order: ")
a = []
for i in range(n):
    i = int(input("Enter number in pocket ["+str(i)+"]"))
    a.append(i)
item = int(input("Enter serch item: "))
index = bserch(a, item)
if index:
    print("Element found in position ", index+1)
else:
    print("not found")                     