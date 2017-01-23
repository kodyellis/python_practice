#!/usr/bin/python
class employee:
    def __init__(self,first,pay):# constructor
        self.first = first
        self.pay = pay
    def info(self):
        return '{}{}'.format(self.first, self.pay)
emp1 = employee('Corey', 544566)


print(emp1.first)
print(emp1.pay)
print(emp1.info())
