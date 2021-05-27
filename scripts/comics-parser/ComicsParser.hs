#!/usr/bin/env stack

import System.Environment (getArgs)
import System.Exit ( ExitCode(ExitFailure), exitSuccess, exitWith )
import Text.ParserCombinators.Parsec

main = getArgs >>= parseArgs >>= putStr . clean

--replace this with a meaningful parser
clean = unlines . lines

parseArgs ["-h"] = usage >> exit
parseArgs [] = getContents
parseArgs fs = concat `fmap` mapM readFile fs

usage = putStrLn "comicsParser file"
exit  = exitSuccess
die   = exitWith (ExitFailure 1)