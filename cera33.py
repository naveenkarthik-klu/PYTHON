score = float(input("Enter score: "))
if score <= 0.0 and score >= 1.0:
    print("Out of range.Please enter a value between 0.0 and 1.0")
    quit()
elif score >= .9 and score < 1.0:
    print("A")
elif score >= .8 and score < .9:
    print("B")
elif score >= .7 and score < .8:
    print("C")
elif score >= .6 and score < .7:
    print("D")
elif score < .6:
    print("F")
