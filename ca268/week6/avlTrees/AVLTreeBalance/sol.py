# When an item is added to an AVL tree it is possible that the tree will become AVL inbalanced.

# For example, when the following items are added to an AVL tree
# [20, 16, 8]

# The AVL tree becomes AVL unbalanced when the 8 is added. The tree is AVL unbalanced at the root node which is 20 and it will be rotated to fix it. Subsequently, the following items are added:
# [10, 5, 12]

# The tree again becomes AVL unbalanced as the 12 is added and it becomes unbalanced at the node with the value 16.

# Your task is to take a sequence of items that are added to an AVL tree and find out which items caused the tree to become unbalanced and which node is unbalanced.

# You should return a list containing the item added and the unbalanced node for each time that the tree becomes unbalanced. For example, in the previous case, the input would be:
# [20, 16, 8, 10, 5, 12]

# And the output should be:
# [(8, 20), (12, 16)]
# Note that there were two occasions when the list became unbalanced, when the 8 and the 12 were added. In those cases, the unbalanced nodes were those with items 20 and 16 respectively.

#
# list of items = [1, 4, 11, 9, 5, 12, 13, 17]
#
def solution():
    return [(11, 1), (5, 11), (12, 4), (13, 11)]