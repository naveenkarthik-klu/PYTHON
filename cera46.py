def computepay(h, r):
    if h > 40:
        reg = h*r
        otp = (h-40.0) * (r*0.5)
        xp = reg+otp
    else:
        xp = h*r

    return xp


hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)
