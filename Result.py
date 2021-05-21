try:
    a = int(input("Enter average: "))
except:
    print("Please enter a number for average")
    exit()
# if a>80 and a<=100:
if 80 < a <= 100:
    print("Pass - Distinction")
# elif a>60 and a<=80:
elif 60 < a <= 80:
    print("Pass - A Class")
# elif a>=40 and a<=60:
elif 40 <= a <= 60:
    print("Pass - B Class")
else:
    print("Fail")
