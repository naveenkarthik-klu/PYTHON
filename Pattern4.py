n = int(input("Enter number of rows: "))
a = int(1)
print('\n')
for i in range(1, n+1):
    for j in range(1, i+1):
        print(a, end=" ")
        a += 1
    print('\n')
