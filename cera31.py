hrs = input("Enter hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h > 40:
    reg = h*r
    otp = (h-40.0) * (r*0.5)
    xp = reg+otp
else:
    xp = h*r
print(xp)
