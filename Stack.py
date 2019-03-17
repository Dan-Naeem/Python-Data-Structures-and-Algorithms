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

s = Stack()
print '* print empty stack'
s.print_stack()
print 'lenth:', s.get_length()
print 'top item:', s.peek()

s.push('alpha')
s.push('bravo')
s.push('charlie')
s.push(5)
s.push(6)
s.print_stack()
print 'lenth:', s.get_length()
print 'top item:', s.peek()

s.pop()
print '* after pop'
s.print_stack()
print 'lenth:', s.get_length()
print 'top item:', s.peek()

s.pop()
print '* after pop'
s.print_stack()
print 'lenth:', s.get_length()
print 'top item:', s.peek()

all = s.get_items()
print all
