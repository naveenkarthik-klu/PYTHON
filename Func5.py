def amg(a):
    s = 0
    while(a > 0):
        r = a % 10
        s = s+r*r*r
        a = a/10
    return s


n = int(input("Enter a number "))
t = n
o = amg(n)
if (int(o) == t):
    print("Armstrong number")
else:
    print("Not a armstrong number")
