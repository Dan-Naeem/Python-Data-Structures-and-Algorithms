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
        # create a new node
        node_to_insert = Node(value)
        # if empty, point root at new node
        if self.is_empty():
            self.root = node_to_insert
        # else find place to insert
        else:
            # create pointer at root
            ptr = self.root
            # go thru tree
            while True:
                # if value is greater, check right child
                if value > ptr.value:
                    # if empty, insert
                    if ptr.right_child == None:
                        ptr.right_child = node_to_insert
                        return
                    # else traverse right subtree
                    ptr = ptr.right_child
                # elif value is less, check left child
                elif value < ptr.value:
                    # if empty, insert
                    if ptr.left_child == None:
                        ptr.left_child = node_to_insert
                        return
                    # else traverse left subtree
                    ptr = ptr.left_child
                # end if/else
            # end while
        # end if/else
    # end def insert()

    def search(self, value):
        #if empty, return
        if self.is_empty():
            return False
        #point at root
        ptr = self.root
        #go thru tree
        while ptr != None:
            # if value == current value
            if value == ptr.value:
                return True
            # elif value is greater than
            elif value > ptr.value:
                # enter right sub tree
                ptr = ptr.right_child
            # elif value is less than
            elif value < ptr.value:
                # enter left sub tree
                ptr = ptr.left_child
        #if exit while loop, value not found
        return False
    # end search()

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

print tree.search(int(raw_input('search for a number: ')))
