#!/usr/bin/env stack

{-# LANGUAGE FlexibleContexts #-}
import Control.Applicative hiding ((<|>))
import System.Environment (getArgs)
import System.Exit ( ExitCode(ExitFailure), exitSuccess, exitWith )
import Text.ParserCombinators.Parsec

main = getArgs >>= parseArgs >>= putStr . clean

--replace this with a meaningful parser
clean :: String -> String
clean = unlines . parse (many1 panel) "ComicsParser"

paddedChar :: Char
paddedChar c = char c <* spaces

data Panel = Panel String String deriving Show

panel :: Parser Panel
panel = do
    speaker <- many1 letter <* paddedChar ':'
    quip <- many1 (noneOf "\n") <* paddedChar '\n'

    tokens <- oneOf "!\"#$%&\'()*+,-./:;<=>?@[]^_`{|}~"

    return $ Panel speaker quip

data ComicWord = String

prettyPrintWord :: ComicWord -> String
prettyPrintWord = show

comicWord :: Parser ComicWord
comicWord = do
    s <- noneOf "!\"#$%&\'()*+,-./:;<=>?@[]^_`{|}~"

    return $ ComicWord

parseArgs ["-h"] = usage >> exit
parseArgs [] = getContents
parseArgs fs = concat `fmap` mapM readFile fs

usage = putStrLn "comicsParser file"
exit  = exitSuccess
die   = exitWith (ExitFailure 1)