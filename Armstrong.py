n = int(input("Enter a number "))
t = n
s = 0
while(n > 0):
    r = n % 10
    s = s+r*r*r
    n = n/10
print("After converting: ", int(s))
# print(s)
if(int(s) == t):
    print(t, " is a armstrong number")
else:
    print(t, " is not a armstrong number")
