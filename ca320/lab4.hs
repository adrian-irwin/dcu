myAppend :: [a] -> [a] -> [a]
myAppend [] [] = []
myAppend [] (y:ys) = y : myAppend [] ys
myAppend (x:xs) [] = x : myAppend xs []
myAppend (x:xs) (y:ys) = x : myAppend xs (y:ys)

myHead :: [a] -> a
myHead [] = error "Empty list"
myHead (x:xs) = x

myLast :: [a] -> a
myLast [] = error "Empty list"
myLast (x:xs) = if null xs
    then x
    else myLast xs

myTail :: [a] -> [a]
myTail [] = error "Empty list"
myTail (x:xs) = xs

myInit :: [a] -> [a]
myInit [] = error "Empty list"
myInit (x:xs) = if null xs
    then []
    else x : myInit xs

myLength :: [a] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

myReverse :: [a] -> [a]
myReverse [] = []
myReverse (x:xs) = myAppend (myReverse xs) [x]

myConcat :: [[a]] -> [a]
myConcat [] = []
myConcat (x:xs) = myAppend x (myConcat xs)

mySum :: Num a => [a] -> a
mySum [] = 0
mySum (x:xs) = x + mySum xs

myProduct :: Num a => [a] -> a
myProduct [] = 1
myProduct [x] = x
myProduct (x:xs) = x * myProduct xs

myMaximum :: Ord a => [a] -> a
myMaximum [] = error "Empty list"
myMaximum [x] = x
myMaximum (x:xs) = if x > myMaximum xs
    then x
    else myMaximum xs

myMinimum :: Ord a => [a] -> a
myMinimum [] = error "Empty list"
myMinimum [x] = x
myMinimum (x:xs) = if x < myMinimum xs
    then x
    else myMinimum xs

myElem :: Eq a => a -> [a] -> Bool
myElem _ [] = False
myElem x (y:ys) = (x == y) || myElem x ys

myDelete :: Eq a => a -> [a] -> [a]
myDelete _ [] = []
myDelete x (y:ys) = if x == y then ys else y : myDelete x ys

myUnion :: Eq a => [a] -> [a] -> [a]
myUnion [] [] = []
myUnion [] (y:ys) = y : myUnion [] ys
myUnion (x:xs) [] = x : myUnion xs []
myUnion (x:xs) (y:ys) = if myElem x (y:ys)
    then myUnion xs (y:ys)
    else x : myUnion xs (y:ys)

myIntersection :: Eq a => [a] -> [a] -> [a]
myIntersection [] [] = []
myIntersection [] (y:ys) = []
myIntersection (x:xs) [] = []
myIntersection (x:xs) (y:ys) = if myElem x (y:ys)
    then x : myIntersection xs (y:ys)
    else myIntersection xs (y:ys)
