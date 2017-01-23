#!/usr/bin/python
print("enter file")
files=input()
print("string you want replace ")
text=input()
print("enter replacement word ")
replace=input()
for line in open(files):
    if text in line:
        line.replace(text,replace)
        print(line)
