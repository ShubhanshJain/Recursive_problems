def length(l):
    if l == []:
        return 0
    return 1+ length(l[1:])

l = ['1','2','3','4','5','6','7','8']
print(length((l)))