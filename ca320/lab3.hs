isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome a =
    a == reverse a

shortest :: (Ord a) => [[a]] -> [a]
shortest [] = []
shortest a =
    minimum a
