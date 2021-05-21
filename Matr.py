print("Enter size of matrix")
m = int(input("Number of rows: "))
n = int(input("Number of columns: "))
mat = []
for i in range(1, m+1):
    for j in range(1, n+1):
        a = int(input("Enter matrix value "))
        mat.append(a)

for i in range(len(mat)):
    print(mat[i], end=" ")
