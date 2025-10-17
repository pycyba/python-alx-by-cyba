import System.Environment

-- Język Haskell. Wersja z tworzeniem tablic.

oblicz::Int -> Int
oblicz n =
    let t1 = [0..n-1] in
    let t2 = [0..n-1] in
    sum([x*y | x <- t1, y <- t2])

main::IO()
main = do
    [arg0] <- getArgs
    let n = read arg0
    let res = oblicz n
    print res
