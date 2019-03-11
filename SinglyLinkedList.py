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
def add_at_index(head, index_to_add, node_to_add):
    """
    Adds a node at a specified index in a list

    Args:
        head (Node)         - head node that points to the list
        index_to_add (int)  - the desired index where teh node is to be added
        not_to_add (Node)   - the node to be added

    Expectations:
        index_to_add should be within range, no out of index error is returned

    Return:
        node that points to the head of the list
    """

    #create pointer
    ptr = head
    #test for edge cases
    #if at head == None
    if ptr == None:
        return head
    #if index_to_add < 0:
    if index_to_add < 0:
        return head
    #if index_to_add == 0
    if index_to_add == 0:
        #if there's a head node (both empty and nonempty)
        if head.value == None:
            #point node_to_add at first node
            node_to_add.next = head.next
            #point head node at node_to_add
            head.next = node_to_add
            #return head node
            return head
        else:
            #point node_to_add at head
            node_to_add.next = head
            #return new head
            return node_to_add
    #check for head node (w/ both empty and nonempty lists)
    if head.value == None:
        #move to next node
        ptr = node.next
    #now ptr should be on the first node, @index == 0
    #go thru list
    next_index = 0
    while ptr != None:
        #increment next_index
        next_index += 1
        #if the next index is the desired index, break
        if next_index == index_to_add:
            break
        #increment pointer
        ptr = ptr.next
    #end while
    #check to see if the next index is the appropriate
    #if exitted while loop before arriving at correct index, dont add node
    if next_index == index_to_add:
        #point node_to_add at next node
        node_to_add.next = ptr.next
        #point current node at node_to_add
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
    # add a new node to the end of the list
    add_at_end(n1, Node('Fox'))
    #print list with index
    print_with_index(n1)
    #test add_at_index()
    print '*** testing add_at_index()'
    index = int(raw_input("Choose an index: "))
    value = '<<< should be %d' % (index)
    test_node = Node(value)
    n1 = add_at_index(n1, index, test_node)
    print_with_index(n1)
################################################################

################################################################
def test_print_edge_cases():
    """Testing for appropriate behavior for edge cases"""

    #case 1: None
    print '*** testing case 1: None'
    case1 = None
    print_list_iterative(case1)
    print_list_recursive(case1)
    print_list_backwards(case1)
    print_with_index(case1)

    #case 2: head node with empty list
    print '*** testing for case 2: head w/ empty list'
    head = Node()
    print_list_iterative(head)
    print_list_recursive(head)
    print_list_backwards(head)
    print_with_index(head)

    '''cases 3 and 4 are expected'''

    #case 3: head node with nonempty list
    print '*** testing for case 3: head node w/ nonempty list'
    head.next = Node('nonempty1')
    head.next.next = Node('nonempty2')
    print_list_iterative(head)
    print_list_recursive(head)
    print_list_backwards(head)
    print_with_index(head)

    #case 4: first node in list
    print '*** testing for case 4: first node in list'
    print_list_iterative(head.next)
    print_list_recursive(head.next)
    print_list_backwards(head.next)
    print_with_index(head.next)
################################################################

################################################################
def create_simple_list():
    """"
    Creates a Simple Linked List

    Args:
        n/a

    Return:
        returns first node in the linked list
    """

    n1 = Node('Alpha')
    n2 = Node('Bravo')
    n3 = Node('Charlie')
    n4 = Node('Delta')
    n5 = Node('Echo')
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    return n1
################################################################

################################################################
def search(head, find_me):
    """
    Searches for a value in the list.

    Args:
        head (Node)      - head node for the list that is to be searched
        find_me (object) - the value that is to be searched for

    Return:
        bool - True if found, False if not
    """
    #create pointer
    ptr = head
    #test for edge cases
    #if none
    if ptr == None:
        return False
    #if head node with empty list
    if ptr.value == None and ptr.next == None:
        return False
    #if head node with nonempty list
    if ptr.value == None and ptr.next != None:
        #increment pointer
        ptr = ptr.next
    #go thru list
    while ptr != None:
        if ptr.value == find_me:
            return True
        #increment pointer
        ptr = ptr.next
    #end while
    return False
################################################################

################################################################
def search_and_replace(head, find_me, replace_with):
    """
    Search for a value and replaces it with another

    Args:
        find_me (object)      - the value to be replaced
        replace_with (object) - the value that replaces

    Return:
        Node that points to the head of the list
    """

    #create a pointer
    ptr = head
    #test for edge cases
    #if None
    if ptr == None:
        return head
    #if head with empty list
    if ptr.value == None and ptr.next == None:
        return head
    #if head node with nonempty list
    if ptr.value == None and ptr.next != None:
        ptr = ptr.next
    #go thru list
    while ptr != None:
        #look for match
        if ptr.value == find_me:
            #replace value
            ptr.value = replace_with
            break
        #increment ptr
        ptr = ptr.next
    #end while
    return head
################################################################

################################################################
def test_search_methods():
    #create linked list
    node = create_simple_list()
    #print list
    print_with_index(node)
    #test search_and_edit()
    find_me = raw_input('search for: ')
    replace_with = raw_input('replace with: ')
    search_and_replace(node, find_me, replace_with)
    print_with_index(node)
################################################################
test_search_methods()
