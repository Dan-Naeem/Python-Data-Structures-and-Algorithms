"""
Stack Implementation w/ python list()
"""

class Stack(object):
    def __init__(self):
        self.items = list()

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_length(self):
        return len(self.items)

    def print_stack(self):
        if not self.is_empty():
            for i in range( len(self.items)-1, -1, -1):
                print self.items[i]
        else:
            print "Stack is Empty"

    def get_items(self):
        return self.items
#end Stack
