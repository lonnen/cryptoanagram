

import System.Environment (getArgs)
import System.Exit ( ExitCode(ExitFailure), exitSuccess, exitWith )
import Text.ParserCombinators.ReadP

main = getArgs >>= parse >>= putStr . clean

--replace this with a meaningful parser
clean = unlines . lines

isColon :: Char -> Bool
isColon char = char == ':'

parse ["-h"] = usage >> exit
parse [] = getContents
parse fs = concat `fmap` mapM readFile fs

usage = putStrLn "comicsParser file"
exit  = exitSuccess
die   = exitWith (ExitFailure 1)