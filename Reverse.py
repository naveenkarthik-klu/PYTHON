n = int(input("Enter a number: "))
r = 0

while n > 0:
    rem = n % 10
    r = r*10+int(rem)
    n = n/10


print(r)
