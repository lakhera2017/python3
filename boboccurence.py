#!/usr/local/bin/python3.6
s = 'azcbobobegghakl'
count = 0
val = len(s)
for i in range(val):
    if s[i:i+3] == "bob":
        count += 1
print("Number of times bob occurs is: " + str(count))
