data BinTree t = Empty | Root t (BinTree t) (BinTree t)
                deriving (Eq, Ord, Show)

leaf x = Root x Empty Empty

addNode :: (Ord a) => a -> BinTree a -> BinTree a
addNode x Empty = leaf x
addNode x (Root y left right)
    | x < y = Root y (addNode x left) right
    | otherwise = Root y left (addNode x right)

maketree :: (Ord a) => [a] -> BinTree a
maketree [] = Empty
maketree [x] = leaf x
maketree (x:xs) = addNode x (maketree xs)

inorder :: BinTree a -> [a]
inorder Empty = []
inorder (Root x left right) = inorder left ++ [x] ++ inorder right

mpsort :: (Ord a) => [a] -> [a]
mpsort x = inorder (maketree x)
