mylist = []
n = int(input("Enter size of array: "))
for i in range(0, n):
    t = int(input("Enter value "))
    mylist.append(t)


print(mylist)

l = len(mylist)
for i in range(0, l):
    print(mylist[i], end=" ")
