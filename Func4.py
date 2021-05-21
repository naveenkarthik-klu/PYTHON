def fact(a):
    f = int(1)
    for i in range(1, a+1):
        f = f*i
    return f


n = int(input("Enter a number "))
r = fact(n)
print("Factorial: ", r)
