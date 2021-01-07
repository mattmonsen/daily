#!/usr/bin/python

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(node.left.right)

s = ""

def serialize(node):
    global s
    if(not node):
        s += "! "
        return s
    s += (str(node.val) + " ")
    s = serialize(node.left)
    s = serialize(node.right)
    return s

i = 0
def deserialize(string):
    global i
    if string[i] == '!':
        if(i < len(string) - 2):
            i += 2
        return None
    else: 
        space = string[i:].find(" ")
        sp = space + i
        node = Node(string[i:sp])
        i = sp + 1
        node.left = deserialize(string)
        node.right = deserialize(string)
        return node


print("Serializing node: " + serialize(node))
print("Assert left left: ", deserialize(serialize(node)).left.left.val == 'left.left')
print("Assert left: ", deserialize(serialize(node)).left.val == 'left')
print("Assert right: ", deserialize(serialize(node)).right.val == 'right')
print("Assert left right: ", deserialize(serialize(node)).left.right == None)
