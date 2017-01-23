#!/usr/bin/python
#fraction Class below
class fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(self.num,"/",self.den)
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
#constructor self is a special parameter that will always be used as a reference back to the object itself.

myfrac = fraction(3,5) #class instance assign to variable
myfrac.show()
myfrac.__str__()
