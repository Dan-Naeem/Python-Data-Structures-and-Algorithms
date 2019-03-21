"""
BinaryMinHeap Implementation
"""
class BinaryMinHeap(object):
    def __init__(self):
        """
        Initializer, doesnt use heap[0]
        """

        self.heap = [None]
        self.last_index = 0

    def is_empty(self):
        return self.last_index == 0

    def insert(self, value):
        # add to the end of the heap
        self.heap.append(value)
        # increment last_index
        self.last_index += 1
        # perc_up item at current index
        self.perc_up(self.last_index)
    # end insert()

    def perc_up(self, index):
        # while there exists a parent node
        while index > 1:
            # calculate parent index, floor result
            parent_index = int( (index) / 2 )
            # if current value < parent value
            if self.heap[index] < self.heap[parent_index]:
                # swap (move smaller value up)
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # move index up to parent node
                index = parent_index
            # else heap order property in maintained
            else:
                return
    # end perc_up()

    def return_min(self):
        return self.heap[1]
    # end return_min()

    def delete_min(self):
        # store minimum
        ret_val = self.return_min()
        # place value at last_index at root of heap
        self.heap[1] = self.heap[self.last_index]
        # decrement last_index
        self.last_index -= 1
        # percolate value at [1] down
        self.perc_down(1)
        # return minimum value
        return ret_val
    # end delete_min()

    def perc_down(self, index):
        # while not at parent of last child (as long as left child exists)
        while (index*2) <= self.last_index:
            # fetch indix of min_child
            min_child = self.min_child(index)
            # if min_child is smaller than current value,
            if self.heap[min_child] < self.heap[index]:
                # swap
                self.heap[min_child], self.heap[index] = self.heap[index], self.heap[min_child]
                # move index down to min_child
                index = min_child
            # else return
            else:
                return
    # end perc_down()

    def min_child(self, index):
        """
        Return index of the smaller child
        """

        # calc child indices
        left_child = i*2
        right_child = (i*2) + 1
        # if right child doesnt exists
        if right_child > self.last_index:
            # return index of left child
            return left_child
        # else determine smaller child, return index
        else:
            # if left child is smaller
            if self.heap[left_child] < self.heap[right_child]:
                return left_child
            # else
            else:
                return right_child
    # end min_child()
# end class BinaryMinHeap()
