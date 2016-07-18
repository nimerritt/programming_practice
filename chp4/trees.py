"""
This module contains common code relating to trees.
"""

class Node:
    """ Representation of a binary tree """

    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right

def treeify(elements):
    """ Takes a strictly increasing sorted list of elements and returns a binary search tree of minimum height. """ 
    if not elements:
        return None
    # find middle index and recurse on subtrees
    n = len(elements)
    i = n // 2
    left = elements[:i]
    mid = elements[i]
    right = elements[i+1:]
    assert(len(left) < len(elements))
    assert(len(right) < len(elements))

    return Node(mid, treeify(left), treeify(right))


