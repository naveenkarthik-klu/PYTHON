largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        print("Invalid input")
        break
    try:
        num = int(num)
        if largest is None or largest < num:
            largest = num
        if smallest is None or smallest > num:
            smallest = num
    except:

        continue
print("Maximum is", largest)
print("Minimum is", smallest)
