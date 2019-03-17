"""
Implementation of Queue using Nodes
"""
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
# end class Node

class Queue(object):
    def __init__(self):
        """Default constructors"""

        self.front = None       # pointer for the front of the queue
        self.rear = None        # pointer for the back of queue
        self.length = 0         # length of queue
        self.max_size = None    # max size of queue, optional
    # end __init__()

    def is_empty(self):
        """Return True id queue is empty."""

        # if length of queue is 0, return True
        return self.length == 0
    # end is_empty()

    def enqueue(self, value):
        """Add an item to the queue."""

        # if max_size is set and has been met, dont enqueue, return
        if self.max_size != None and self.length == self.max_size:
            return

        # otherwise continue as normal, enqueue
        if self.is_empty():
            # point both front and rear pointers the new value
            self.front = Node(value)
            self.rear = self.front
            # increment length
            self.length += 1
        # elif not empty
        else:
            # add a new Node to the end of the queue
            self.rear.next = Node(value)
            # increment rear pointer and length
            self.rear = self.rear.next
            self.length += 1
    # end enqueue()

    def dequeue(self):
        """Remove and return an item from the queue."""

        # if not empty
        if not self.is_empty():
            # capture the value to be returned
            ret_val = self.front.value
            # point front pointer at next node, delete node
            temp = self.front
            self.front = self.front.next
            # decrement length
            self.length -= 1
            # return value
            return ret_val
    # end dequeue()

    def get_length(self):
        """Returnt the length of the queue."""

        return self.length
    # end get_length()

    def peek(self):
        """Return the head of the queue."""

        # if not empty
        if not self.is_empty():
            # return first item
            return self.front.value
    # end peek()

    def print_(self):
        """Print the Queue"""

        # if not empty
        if not self.is_empty():
            #create a pointer
            ptr = self.front
            # go thru queue
            while ptr != None:
                # print value at each node
                print ptr.value
                # increment pointer
                ptr = ptr.next
        else:
            print 'Empty Queue'
    # end print_
# end class Queue

q = Queue()
q.print_()
print

q.enqueue('Alpha')
q.enqueue('Bravo')
q.enqueue('Charlie')
q.print_()
print 'length', q.get_length()
print 'peek', q.peek()
print

print 'deq', q.dequeue()
print 'new length', q.get_length()
print 'new peek', q.peek()
print

print 'updated queue'
q.print_()
print

q.dequeue()
q.dequeue()
q.print_()
