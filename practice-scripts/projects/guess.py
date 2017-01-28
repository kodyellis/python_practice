#!/usr/bin/python3
# The program will first randomly generate a number unknown to the user.
import random

print("Enter a number")
userPut = input()

cguess = int(random.random()*100)
# print(cguess)

if cguess == userPut:
    print("Correct:%s" % userPut)
else:
    print("Wrong, the right ans:%s" % cguess)
