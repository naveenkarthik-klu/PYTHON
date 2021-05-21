def add(a, b):
    c = a+b
    return c


def sub(a, b):
    c = a-b
    return c


def mult(a, b):
    c = a*b
    return c


def div(a, b):
    c = a/b
    return c


x = int(input("Enter num1 "))
y = int(input("Enter num2 "))
try:
    o = int(input("1.Add 2.Subtract 3.Multiply 4.Divide "))
except:
    print("Enter a number for your choice")
    exit()
if o == 1:
    z = add(x, y)
    print("Result ", z)
elif o == 2:
    z = sub(x, y)
    print("Result ", z)
elif o == 3:
    z = mult(x, y)
    print("Result ", z)
else:
    z = div(x, y)
    print("Result ", z)
