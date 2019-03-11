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
def print_with_index(node):
    """
    Print all items in a linked list alongside the index.

    Param
    -----
        Expects a pointer to the head of the list

    Return
    ------
        Returns nothing
    """

    #create a pointer
    ptr = node
    #test for exit conditions
    #if at end of list (None)
    if ptr == None:
        return
    #if at head node with empty list
    if ptr.value == None and ptr.next == None:
        return
    #if at head node with nonempty list
    if ptr.value == None and ptr.next != None:
        ptr = ptr.next
    #create counter, go thru list
    counter = 0
    while ptr != None:
        print counter, ptr.value
        #increment counter and pointer
        counter += 1
        ptr = ptr.next
################################################################

################################################################
def print_list_recursive(node):
    """Print a Singly Linked List using recursion."""

    #if at end of list
    if node == None:
        return
    #if at head node with empty list
    elif node.value == None and node.next == None:
        return
    #if at head node with nonempty list
    elif node.value == None and node.next != None:
        #recursive call on next node
        print_list_recursive(node.next)
    #if at a node within the list
    else:
        #print, recusrive call on next node
        print node.value
        print_list_recursive(node.next)
################################################################

################################################################
def print_list_backwards(node):
    """Print a Singly Linked List backwards using recursion."""

    #if at end of list
    if node == None:
        return
    #if at head node with empty list
    elif node.value == None and node.next == None:
        return
    #if at head node with nonempty list
    elif node.value == None and node.next != None:
        print_list_backwards(node.next)
    #if at a node within the list
    else:
        #recursive call on next node, then print
        print_list_backwards(node.next)
        print node.value
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
    print 'print list backwards'
    print_list_backwards(l1)
################################################################

################################################################
def add_at_end(head, node_to_add):
    """
    Adds a node to the end of the list.

    Param
    -----
        Expects a pointer to the head of the list and the node to be added

    Return
    ------
        Returns a pointer to the head of the list
    """

    #create pointer
    ptr = head
    #check if at none
    if ptr == None:
        return
    #check if at head node with empty list
    if ptr.value == None and ptr.next == None:
        return
    #check if at head node with nonempty list
    if ptr.value == None and ptr.next != None:
        #increment pointer
        ptr = ptr.next
    #go thru list, while not at the last node
    while ptr.next != None:
        ptr = ptr.next
    #at last node
    ptr.next = node_to_add
    return head
################################################################

################################################################
def test_add_node_to_list():
    """Tests funcitonality of adding a node to a linked list."""

    #create nodes
    n1 = Node('Alpha')
    n2 = Node('Bravo')
    n3 = Node('Charlie')
    n4 = Node('Delta')
    n5 = Node('Echo')
    #link them
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    #print list
    print_list_iterative(n1)
    print_with_index(n1)
    # add a new node to the end of the list
    newNode = Node(raw_input('Enter a value to be added to list: '))
    add_at_end(n1, newNode)
    #print list again
    print '*** after add_at_end()'
    print_list_iterative(n1)
    #print list with indices
    print 'testing print with index'
    print_with_index(n1)
################################################################
test_add_node_to_list()
