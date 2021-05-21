print("Odd/Even")
a = int(input("Enter a number: "))
if a % 2 == 0:
    print("Given number is an even number")
else:
    print("Given number is an odd number")
print("Positive/Negative")
b = int(input("Enter a number: "))
if b > 0:
    print("Given number is a positive number")
elif b < 0:
    print("Given number is a negative number")
else:
    print("Given number is neither positive nor negative")
