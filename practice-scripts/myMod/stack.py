#!/usr/bin/python3
class Stack():
    def __init__(self):
        self.items = [] #this function init. the array item
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []

#creating Instances

s = Stack()
print(s.is_empty())
s.push(4)
s.push("Dog")
print(s.is_empty())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.size())
