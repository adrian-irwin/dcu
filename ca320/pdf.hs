
rectangleArea :: Float -> Float -> Float
rectangleArea x y = x * y

doubleSmallNumber :: Int -> Int
doubleSmallNumber x = if x > 100
                        then x
                        else x*2

incDoubleSmallNumber :: Int -> Int
incDoubleSmallNumber x = (if x > 100 then x else x*2) + 1


listLength :: (Integral b) => [a] -> b
-- base case, empty list
listLength [] = 0
-- pattern match for a list with something at the start(head) followed by a tail (_:xs)
listLength (_:xs) = 1 + listLength xs
-- _ is the head, _ is used when we don't care about the value at that location
-- xs is the tail of the list
-- if we only have one item in the list, the list internally looks as such, 1:[]

capital :: String -> String
capital "" = "Empty string, whoops!"
capital test@(x:xs) = "The first letter of " ++ test ++ " is " ++ [x]


bmiTell1 :: (RealFloat a) => a -> a -> String
bmiTell1 weight height
    | weight / height ^ 2 <= 18.5 = "Have a steak!"
    | weight / height ^ 2 <= 25.0 = "Supposedly normal!"
    | weight / height ^ 2 <= 30.0 = "How about a walk?"
    | otherwise            = "Skip that snack"


bmiTell2 :: (RealFloat a) => a -> a -> String
bmiTell2 weight height
    | bmi <= skinny = "Have a steak!"
    | bmi <= normal = "Supposedly normal!"
    | bmi <= comfortable = "How about a walk?"
    | otherwise = "Skip that snack"
    where bmi = weight / height ^ 2
          (skinny, normal, comfortable) = (18.5, 25.0, 30.0)

initials :: String -> String -> String
initials firstname lastname =
    [f] ++ ". " ++ [l] ++ "."
    where (f:_) = firstname
          (l:_) = lastname

cylinderArea :: (RealFloat a) => a -> a -> a
cylinderArea r h =
    let sideArea = 2 * pi * r * h
        topArea  = pi * r^2
    in  sideArea + 2 * topArea

headOfList :: [a] -> a
headOfList xs = case xs of []   -> error "Empty list!"
                           (x:_)-> x

takeList :: (Num i, Ord i) => i -> [a] -> [a]
takeList n _
        | n <= 0 = []
takeList _ [] = []
takeList n (x:xs) = x : takeList (n-1) xs

reverseList :: [a] -> [a]
reverseList [] = []
reverseList (x:xs) = reverseList xs ++ [x]

reverseListAcc :: [a] -> [a] -> [a]
reverseListAcc [] x = x
reverseListAcc (x:xs) y = reverseListAcc xs (x:y)

reverseList2 :: [a] -> [a]
reverseList2 x = reverseListAcc x []

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
    let smallerSorted = quicksort [a | a <- xs, a <= x]
        biggerSorted = quicksort [a | a <- xs, a > x]
    in smallerSorted ++ [x] ++ biggerSorted

comparehi = compare 100
comparelo = compare 20

checkThresholds :: (Num a) => a -> (a->Ordering) -> (a-> Ordering) -> String
checkThresholds x hi lo
    | high = "too high"
    | low = "too low"
    | otherwise = "OK"
    where (high, low) = (hi x == LT, lo x == GT)

-- lambda functions = (\x -> thing x ) 21
-- e.g. length (filter (\xs -> length xs > 15) [1..100]) this lambda function only accepts the items that are greater than 15 from the list

