test = "X-DSPAM-Confidence:    0.8475"
t = test.find('0.8475')
print(t)
print(float(test[23:29]))
