"""
Use my stack implementation to devise an algorithm to check if parenthees are balanced
"""

from Stack import Stack

def is_balanced_paren(input_string):
    """
    Checks to see whether or not an input strings has balanced set of parentheses.

    Param:
        input_string (string): the input string to be tested

    Return:
        balanced (bool): return True if parentheses are balanced

    Conditions:
        expects a string
        works as advertised on an empty string and a string with no parentheses
    """

    #create a dictionary to store paren pairs
    pairs = {"(":")", "[":"]", "{":"}"}
    #create an empty stack
    s = Stack()
    #create a flag to track if input_string in balanced
    balanced = True
    #go thru every letter in the string
    for letter in input_string:
        #if an open paren
        if letter in "([{":
            #push appr pair onto stack
            s.push(letter)
        #if close paren
        if letter in "}])":
            #if stack is empty
            if s.is_empty():
                #not balanced
                balanced = False
                return balanced
            #elif not empty
            else:
                #pop from stack
                top_letter = s.pop()
                #if not match
                if letter != pairs[top_letter]:
                    #not balanced
                    balanced = False
                    return balanced
            #end if/else
        #end if/else
    #end for loop
    #if stack is not empty
    if not s.is_empty():
        #not balanced
        balanced = False
    return balanced
#end def is_balanced_paren()


mylist = [
    "",                 # 0 True
    "no parentheses",   # 1 True
    "()",               # 2 True
    "[]",               # 3 True
    "{}",               # 4 True
    "(]",               # 5 False
    "}}",               # 6 False
    "(){}[([])]",       # 7 True
    "(()",              # 8 False
    "())",              # 9 False
    "()[]",             # 10 True
    "{[{[{[{[{[{[]]}]}]}]}]}]}",            # 11 False
    "({({({({({({({({({})})})})})})})})})", # 12 True
]

results = list()

for item in mylist:
    results.append(is_balanced_paren(item))

for index, x, in enumerate(results):
    print index, x
