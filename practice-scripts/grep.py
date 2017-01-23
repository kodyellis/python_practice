#!/usr/bin/python
print("enter file")
files=input()
print("string being searched")
text=input()
for line in open(files):
    if text in line:
        print(line)
