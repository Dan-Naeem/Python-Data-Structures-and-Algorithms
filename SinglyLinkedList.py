################################################################
class Node(object):
    def __init__(self, value=None, next=None):
        """Initializes value and next to None by default."""

        self.value = value
        self.next = next
################################################################

################################################################
def create_linked_list():
    """Creates a linked list with user input."""

    n = int(raw_input("How many item do you want to add: "))
    l1 = Node()
    ptr = l1
    for i in range(n):
        #create a new node, point to it
        ptr.next = Node(raw_input('Enter a value: '))
        #increment pointer
        ptr = ptr.next
    #print list
################################################################
create_linked_list()
