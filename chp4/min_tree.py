# Exercise 4.2 from CtCI 6th Edition
# Nicholas Merritt

""" Minimal Tree: Given a sorted (increasing order) array with unique
integer elements, write an algorithm to create a binary search tree with
minimal height. """

class Node:
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right

def verify_binary_tree(root):
    if not root:
        return True
    left = root.left and root.left.label < root.label and verify_binary_tree(root.left) or True
    right = root.right and root.right.label > root.label and verify_binary_tree(root.right) or True

    return left and right

def treeify(elements):
    """ Takes a strictly increasing sorted list of elements and returns a binary search tree. """ 
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

t = treeify(list(range(10)))
assert(verify_binary_tree(t) == True)
