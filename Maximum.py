def numbers(a, l, maximum):
    if l <0:
        return maximum
    else:
        if a[l] > maximum: # reverse comparision
            maximum = a[l]
    return numbers(a, l-1, maximum) # every iteration value of l is reduced to continue backward comparision

a = [1, 6, 5, 7, 34, 46, 76, 99]
maximum = a[0]  # max value set to  first index value
l = len(a) -1

print(numbers(a, l, maximum))        