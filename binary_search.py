"""
Binary search on a sorted array (python list())
"""

def binary_search(value, arr):
    """
    Employs binary search to find the index of a value in a list.

    Param:
        value (int) - specified value to be searched for

    Return:
        (int)       - return the index of the value if a match is found, else -1
    """

    # set left and right bounds
    l = 0
    r = len(arr) - 1
    # start binary search
    while True:
        # break condition
        if r < l:
            return -1
        # find middle index
        mid = int(r - ( (r-l) / 2 ))
        # compare againt value at mid
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            # raise left bound
            l = mid + 1
        elif value < arr[mid]:
            # lower right bound
            r = mid - 1
# end binary_search()

my_array = [
    1, # 0
    2,
    3,
    4,
    5,
    7,  # 5
    9,
    10,
    13,
    15,
    16, # 10
    17,
    17,
    18,
    21,
    22, # 15
    24,
    25,
    28,
    31,
    32, # 20
    34,
    36,
    37,
    38,
    38, # 25
    38,
    40,
    41,
    44 # 29
]
while True:
    # must input a number
    find_num = int(raw_input("What number are you searching for: "))
    index =  binary_search(find_num, my_array)
    if index == -1:
        print 'Number not found'
    else:
        print 'my_array[%d] = %d' % (index, my_array[index])
