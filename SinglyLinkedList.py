################################################################
class Node(object):
    def __init__(self, value=None, next=None):
        """Initializes value and next to None by default."""

        self.value = value
        self.next = next
################################################################

################################################################
def print_list_iterative(node):
    """Print a Singly Linked List, iterative traversal."""

    #create a pointer
    ptr = node
    #if at None
    if ptr == None:
        return
    #if at head node, and empty list
    elif ptr.value == None and ptr.next == None:
        return
    #if at head node, and nonempty list
    elif ptr.value == None and ptr.next != None:
        ptr = ptr.next
    #while at a node within the list
    while ptr != None:
        print ptr.value
        ptr = ptr.next
################################################################

################################################################
def print_list_recursive(node):
    """Print a Singly Linked List using recursion"""

    #if at end of list
    if node == None:
        return
    #if at head node with empty list
    elif node.value == None and node.next == None:
        return
    #if at head none with nonempty list
    elif node.value == None and node.next != None:
        #recursive call on next node
        print_list_recursive(node.next)
    #if at a node within list
    else:
        #print, recusrive call on next node
        print node.value
        print_list_recursive(node.next)
################################################################

################################################################
def create_linked_list():
    """Creates a linked list with user input."""

    n = int(raw_input("How many items do you want to add: "))
    l1 = Node()
    ptr = l1
    for i in range(n):
        #create a new node, point to it
        ptr.next = Node(raw_input('Enter a value: '))
        #increment pointer
        ptr = ptr.next
    #print list
    print 'print list iter'
    print_list_iterative(l1)
    print 'print list recur'
    print_list_recursive(l1)
################################################################
create_linked_list()
