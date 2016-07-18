# Exercise 4.2 from CtCI 6th Edition
# Nicholas Merritt

from trees import Node, treeify

""" Minimal Tree: Given a sorted (increasing order) array with unique
integer elements, write an algorithm to create a binary search tree with
minimal height. """

def verify_binary_tree(root):
    if not root:
        return True
    left = root.left and root.left.label < root.label and verify_binary_tree(root.left) or True
    right = root.right and root.right.label > root.label and verify_binary_tree(root.right) or True

    return left and right

t = treeify(list(range(10)))
assert(verify_binary_tree(t) == True)
