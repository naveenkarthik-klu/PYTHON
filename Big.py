a = int(input("Enter 'a' value: "))
b = int(input("Enter 'b' value: "))
c = int(input("Enter 'c' value: "))
if a > b:
    if a > c:
        print("a is big")
    else:
        print("c is big")
else:
    if b > c:
        print("b is big")
    else:
        print("c is big")
