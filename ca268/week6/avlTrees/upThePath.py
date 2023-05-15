from Node import Node

#
#   Function to add an item to a tree.
#
#   This is not good object oriented coding. It's not even very polite. It directly interferes with the tree's innards.
#
def add(tree, item):
    """ Add this item to its correct position on the tree """
    # This is a non recursive add method. A recursive method would be cleaner.
    if tree.root == None: # ... Empty tree ...
        tree.root = Node(item, None, None) # ... so, make this the root
    else:
        # Find where to put the item
        parentStack = []
        child_tree = tree.root
        while child_tree != None:
            parentStack.append(child_tree)
            parent = child_tree
            if item < child_tree.item: # If smaller ...
                child_tree = child_tree.left # ... move to the left
            elif item > child_tree.item:
                child_tree = child_tree.right

        # child_tree should be pointing to the new node, but we've gone too far
        # we need to modify the parent nodes
        n = Node(item, None, None)
        if item < parent.item:
            parent.left = n
        elif item > parent.item:
            parent.right = n
        # Ignore the case where the item is equal.

        while n != None:
            if abs(tree.recurse_height(n.left) - tree.recurse_height(n.right)) > 1:
                return n.item
            if len(parentStack) == 0:
                n = None
            else:
                n = parentStack.pop()

    # return parentStack
    # a = tree.root
    # while a != None:
    #     if -1 <= tree.recurse_height(a.left) - tree.recurse_height(a.right) <= 1:


    # prev = 0
    # while a != None:
    #     balanced = tree.recurse_height(a.left) - tree.recurse_height(a.right)
    #     if balanced > 1:
    #         print(f"right balanced = {balanced}")
    #         prev = a.item
    #         a = a.left
    #     elif balanced < -1:
    #         print(f"left balanced = {balanced}")
    #         prev = a.item
    #         a = a.right
    #     else:
    #         return prev

        # prev = a
        # print(f"left height: {tree.recurse_height(a.left)}")
        # print(f"right height: {tree.recurse_height(a.right)}")
        # # print(f"left item: {a.left.item}")
        # # print(f"right item: {a.right.item}")
        # if (a.left == None or a.right == None) or (tree.recurse_height(a.right) - tree.recurse_height(a.left) > 1) or (tree.recurse_height(a.left) - tree.recurse_height(a.right) > 1):
        #     return a.item
        # if tree.recurse_height(a.right) > tree.recurse_height(a.left):
        #     a = a.right
        # else:
        #     a = a.left
        # print(f"next a = {a.item}\n")
        # a = None

    # print(abc.left.item)
    # while tree.recurse_height(abc.right) < 2 or tree.recurse_height(abc.left) < 2:
    # while abc.right != None or abc.left != None:
    #     if tree.recurse_height(abc.right) > tree.recurse_height(abc.left):
    #         abc = abc.right
    #     else:
    #         abc = abc.left

    # # print(abc.item)

    # print(tree.recurse_height(tree.root.right), tree.root.right.item)
    # print(tree.recurse_height(tree.root.left), tree.root.left.item)
    # print("")
    # print(tree.recurse_height(tree.root.right.right), tree.root.right.right.item)
    # print(tree.recurse_height(tree.root.right.left), tree.root.right.left.item)
    #   Note that you can get the height of a node by calling tree.recurse_height().
    #       For example, the height of the root is tree.recurse_height(tree.root)
    #
