"""
Question 4.3 from Cracking the Coding Interview 6th Edition

List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists). 
"""

import trees

def depths(root, depth_lists, depth):
    # invariant 1: depth_lists contains at least 'depth' elements
    # base case
    if not root:
        return depth_lists

    # enforce inv. 1
    if len(depth_lists) <= depth:
        depth_lists.append([])

    depth_lists[depth].append(root.label)
    depths(root.left, depth_lists, depth + 1)
    depths(root.right, depth_lists, depth + 1)

    return depth_lists

t = trees.treeify(list(range(10)))

lists = []
depths(t, lists, 0)
print(lists)



