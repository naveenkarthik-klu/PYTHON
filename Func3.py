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

p = add(x, y)
print("Addition ", p)
q = sub(x, y)
print("Subtraction ", q)
r = mult(x, y)
print("Multiplication ", r)
s = div(x, y)
print("Division ", s)
