data AVLTree a = Empty | Root a (AVLTree a) (AVLTree a)
                deriving (Show, Eq, Ord)

-- insert a value into the tree
insert :: (Ord a) => a -> AVLTree a -> AVLTree a
insert x Empty = Root x Empty Empty
insert x (Root y l r)
    | x < y = balance (Root y (insert x l) r)
    | otherwise = balance (Root y l (insert x r))

-- four cases to balance for: left left, left right, right left, right right
balance :: (Ord a) => AVLTree a -> AVLTree a
balance Empty = Empty
balance (Root x l r)
    -- left left
    | checkBalance (Root x l r) && height (getRightTree l) < height (getLeftTree l) = rotateRight (Root x l r)
    -- left right
    | checkBalance (Root x l r) && height (getRightTree l) > height (getLeftTree l) = rotateRight (Root x (rotateLeft l) r)
    -- right right
    | checkBalance (Root x l r) && height (getLeftTree r) < height (getRightTree r) = rotateLeft (Root x l r)
    -- right left
    | checkBalance (Root x l r) && height (getLeftTree r) > height (getRightTree r) = rotateLeft (Root x l (rotateRight r))
    -- no rotation needed
    | otherwise = Root x l r

-- find the height of a tree
height :: AVLTree a -> Int
height Empty = 0
height (Root _ l r) = 1 + max (height l) (height r)

-- check the tree's balance factor
checkBalance :: AVLTree a -> Bool
checkBalance Empty = True
checkBalance (Root _ l r) = abs (height l - height r) >= 1

-- get value of root of given tree
getValue :: AVLTree a -> a
getValue Empty = error "Empty tree"
getValue (Root x _ _) = x

-- get the right sub tree of a given tree
getRightTree :: AVLTree a -> AVLTree a
getRightTree Empty = Empty
getRightTree (Root _ _ r) = r

-- get the left sub tree of a given tree
getLeftTree :: AVLTree a -> AVLTree a
getLeftTree Empty = Empty
getLeftTree (Root _ l _) = l

-- rotate the tree to the left
rotateLeft :: (Ord a) => AVLTree a -> AVLTree a
rotateLeft Empty = Empty
rotateLeft (Root x l r) = Root (getValue r) (Root x l (getLeftTree r)) (getRightTree r)

-- rotate the tree to the right
rotateRight :: (Ord a) => AVLTree a -> AVLTree a
rotateRight Empty = Empty
rotateRight (Root x l r) = Root (getValue l) (getLeftTree l) (Root x (getRightTree l) r)

-- pass the give tree to the helper function then print the result
printTree :: (Show a) => AVLTree a -> IO ()
printTree x = putStr (unlines (printTreeHelper x 0))

-- helper function that puts each node into a string list with the correct indentation
printTreeHelper :: (Show a) => AVLTree a -> Int -> [String]
printTreeHelper Empty _ = []
printTreeHelper (Root x l r) n =
    printTreeHelper l (n + 1) ++
    [replicate (n * 5) ' ' ++ show x] ++
    printTreeHelper r (n + 1)