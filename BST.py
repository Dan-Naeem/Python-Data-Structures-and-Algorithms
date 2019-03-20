"""
Implementation of a Binary Search Tree
"""
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
# end class Node()

class BinarySearchTree(object):
    def __init__(self, node=None):
        self.root = node

    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False

    def insert(self, value):
        # if empty, point root at new node
        if self.is_empty():
            self.root = Node(value)
        # else find place to insert
        else:
            # call recursive insert function on root
            self.__insert(value, self.root)
    # end def insert()

    def __insert(self, value, ptr):
        """Helper insert function, recursive."""
        # if greater, check right
        if value > ptr.value:
            # if right is None, insert
            if ptr.right_child == None:
                ptr.right_child = Node(value)
            # else recursive call on right child
            else:
                self.__insert(value, ptr.right_child)
        # if less, check left
        elif value < ptr.value:
            # if left is None, insert
            if ptr.left_child == None:
                ptr.left_child = Node(value)
            # else recursive call on left child
            else:
                self.__insert(value, ptr.left_child)
        # else if equal, return
        else:
            #Do not insert duplicate elements
            return
    # end __insert()

    def search(self, value):
        # if empty, return False
        if self.is_empty():
            return False
        # else recursive call on root
        else:
            return self.__search(value, self.root)
    # end search()

    def __search(self, value, ptr):
        """Helper search function, recursive."""
        if ptr == None:
            return False
        else:
            if value == ptr.value:
                return True
            elif value > ptr.value:
                return self.__search(value, ptr.right_child)
            else:
                return self.__search(value, ptr.left_child)
    # end __search()

    def print_(self, traversal='inorder'):
        # if empty
        if self.is_empty():
            print 'EMPTY TREE'
        # elif not empty
        else:
            # check desired traversal type
            if traversal == 'inorder':
                self.__print_inorder(self.root)
            if traversal == 'inorder-style':
                self.__print_inorder_stylized(self.root)
            elif traversal == 'preorder':
                self.__print_preorder(self.root)
            elif traversal == 'postorder':
                # not implemented yet
                pass
    # end print_inorder

    def __print_inorder(self, ptr):
        #if not at None:
        if ptr != None:
            self.__print_inorder(ptr.left_child)
            print ptr.value
            self.__print_inorder(ptr.right_child)
    # end def __print_inorder()

    def __print_inorder_stylized(self, ptr, line=""):
        #if not at None:
        if ptr != None:
            next_line = line+"    "
            self.__print_inorder_stylized(ptr.right_child, (next_line))
            print line, '  /'
            print line, ptr.value
            print line, '  \\'
            self.__print_inorder_stylized(ptr.left_child, (next_line))
    # end def __print_inorder()

    def __print_preorder(self, ptr, line="|_"):
        # if not at None
        if ptr != None:
            print line[:len(line)-1]
            print line, ptr.value
            line = "   " + line
            self.__print_preorder(ptr.left_child, line)
            self.__print_preorder(ptr.right_child, line)
# end class BinsarySearchTree()


tree = BinarySearchTree()

tree.insert(9)
tree.insert(10)
tree.insert(15)
tree.insert(3)
tree.insert(4)
tree.insert(7)
tree.insert(12)
tree.insert(5)
tree.insert(8)
tree.insert(14)

print 'inorder stylized'
tree.print_('inorder-style')
print ""

print 'print preorder'
tree.print_('preorder')
print ""

print 'print inorder'
tree.print_()
print ""

for i in range(21):
    if tree.search(i):
        print i, '*'
    else:
        print i
