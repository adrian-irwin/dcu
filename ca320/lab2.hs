triangleArea :: Float -> Float -> Float -> Float
triangleArea a b c =
    let s = (a + b + c) / 2
    in sqrt (s * ((s - a) * (s - b) * (s - c)))

triangleAreaError :: Float -> Float -> Float -> Float
triangleAreaError a b c
    | not (isNaN t) = sqrt t
    | isNaN (sqrt t) = error "Not a triangle"
    where s = (a + b + c) / 2
          t = sqrt (s * ((s - a) * (s - b) * (s - c)))

isSum :: Int -> Int -> Int -> Bool
isSum a b c
    | a + b == c = True
    | a + c == b = True
    | b + c == a = True
    | otherwise = False