fname = input("Enter file name: ")
fh = open(fname)
for l in fh:
    l2 = l.rstrip()
    print(l2.upper())
