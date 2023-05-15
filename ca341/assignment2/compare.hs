-- type definition for a binary tree that will be used throughout the program
data BinTree t = Empty | Root t (BinTree t) (BinTree t)
                deriving(Ord, Eq, Show)

insert :: (Ord a) => a -> BinTree a -> BinTree a
-- insert takes an element and a tree and returns a tree with the element inserted
insert x Empty = Root x Empty Empty -- if the tree is empty, insert the element at the root
insert x (Root y left right) -- if the tree is not empty, compare the element to the root
    | x < y = Root y (insert x left) right
    | otherwise = Root y left (insert x right)

search :: (Eq a, Ord a) => a -> BinTree a -> Bool
-- search takes an element and a tree and returns True if the element is in the tree
search x Empty = False -- if the tree is empty, the element is not in the tree
search x (Root y left right) -- if the tree is not empty, compare the element to the root
    | x == y = True -- if the element is equal to the root, the element is in the tree
    -- if the element is less than the root, search the left subtree, otherwise search the right subtree
    | x < y = search x left
    | x >= y = search x right
    | otherwise = False -- if the element is not found in the left or right subtree, the element is not in the tree

preorder :: BinTree t -> [t]
-- preorder takes a tree and returns a list of the elements in the tree in preorder traversal
preorder Empty = [] -- if the tree is empty, return an empty list
preorder (Root x left right) = [x] ++ preorder left ++ preorder right -- if the tree is not empty, return the root then recursively call preorder on the left and right subtrees

postorder :: BinTree t -> [t]
-- postorder takes a tree and returns a list of the elements in the tree in postorder traversal
postorder Empty = [] -- if the tree is empty, return an empty list
postorder (Root x left right) = postorder left ++ postorder right ++ [x] -- if the tree is not empty, recursively call postorder on the left and right subtrees then return the root

inorder :: BinTree t -> [t]
-- inorder takes a tree and returns a list of the elements in the tree in inorder traversal
inorder Empty = [] -- if the tree is empty, return an empty list
inorder (Root x left right) = inorder left ++ [x] ++ inorder right -- if the tree is not empty, recursively call inorder on the left subtree then return the root then recursively call inorder on the right subtree