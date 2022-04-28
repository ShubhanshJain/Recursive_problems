def product(m ,n):
    if n == 1:
        return m
    return m +product(m , n-1)
m = int(input("Enter a number: "))
n = int(input("Enter a number: "))
print("Product if numbers is: ", product(m,n))