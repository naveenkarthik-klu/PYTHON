e = []
n = int(input("Enter number of values: "))
print("Enter the values:")
for i in range(0, n):
    t = int(input())
    e.append(t)

print("Ascending sort:")
for i in range(0, n):
    for j in range(i+1, n):
        if(e[i] > e[j]):
            s = e[i]
            e[i] = e[j]
            e[j] = s


l = len(e)
for i in range(0, l):
    print(e[i], end=" ")


print("\nDescending sort:")
for i in range(0, n):
    for j in range(i+1, n):
        if(e[i] < e[j]):
            s = e[i]
            e[i] = e[j]
            e[j] = s


l = len(e)
for i in range(0, l):
    print(e[i], end=" ")
