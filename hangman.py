#!/usr/bin/python

#Your Everyday Hangman Game
#Author: Peter Vlasveld
#Date: 19/01/2019

import random
import re

#gets the word to be displayed to the screen either
# masked by asterisks or not
def getWord (disWord, wordBool):
    retStr = ""
    for i in xrange(0, len(disWord)):
        if wordBool[i]:
            retStr += disWord[i:i+1]
        else:
            retStr += '*'
    return retStr

#prints the current hangman to screen
def printHangman (strikes):
    print "____"
    strikeList = [
        ["|   "]*4,
        ["|  |","|   ","|   ","|   "],
        ["|  |","|  0","|   ","|   "],
        ["|  |","|  0","|  |","|   "],
        ["|  |","|  0","| /|","|   "],
        ["|  |","|  0","| /|\\","|   "],
        ["|  |","|  0","| /|\\","| / "],
        ["|  |","|  0","| /|\\","| / \\"],
    ]
    for i in strikeList[strikes]:
        print i
    print "|____"

#prints a hangman graphic when the player dies
def printDead ():
	print " _________.._____"
	print "|._________))____|"
	print "|| //      ||"
	print "||//       ||  "
	print "||/        ||.-''."
	print "||         |/  _   \\"
	print "||         ||  `/, |"
	print "||         (\\\\`_.'"
	print "||        .-`--'"
	print "||       /Y . . Y\\\\"
	print "||      // |   |  \\\\"
	print "||     //  | . |   \\\\"
	print "||    ')   |   |    (`"
	print "||         ||'||"
	print "||         || ||"
	print "||         || ||"
	print "||         || ||"
	print "||        / | | \\"
	print "''''''''|_`-' `-' |'''|"
	print "||''''''\\\\        '''||"
	print "||       \\\\          ||"
	print "::        \\\\         ::   sk"
	print "..         `'        .."
	return

#returns a wordlist for a given topic
def getWords (topic):
    filename = ""
    if topic == '1':
        filename = "dicWords.txt"
    elif topic == '2':
        filename = "progWords.txt"
    f1 = open(filename)
    content = f1.readlines()
    f1.close()
    return content

#function for allowing the player to guess the whole word
def guessWord(word):
    inp = raw_input("Word:")
    if inp.lower() == word:
        return True
    return False

#welcome message
print "Welcome to Hangman!\n"

#main game loop
playing = True
while(playing == True):
    #Opening menu
    print "Please choose a topic:"
    print "1. Dictionary words"
    print "2. Programming languages"
    topic = raw_input("Choice:")
    while not re.match("^[12]$", topic):
        topic = raw_input("Invalid input, please try again")

    #set and declare game variables
    words = getWords(topic)
    rand = random.randint(0,len(words)-1)
    word = words[rand].lower().rstrip()
    disWord = words[rand].rstrip()
    wordBool = [False]*len(word)
    guesses = []
    first = True
    lives = 7
    strikes = 0
    won = False

    #game loop
    while strikes < 7:
        #display word, guesses and hangman
        print("Word: " + getWord(disWord, wordBool))
        if not first:
            print("Guessed: " + str(guesses))
        first = False
        printHangman(strikes)
        print "Type 'guess' to guess the whole word."
        print "Type 'exit' to exit the game."

        #get a letter and make sure its a letter
        inp = raw_input("Guess a letter: ")

        #allow the player to guess at any point
        if inp == 'guess':
            if guessWord(word):
                won = True
                break
            else:
                print("Incorrect word.")
                continue
        
        #allow the player to exit at any point
        if inp == 'exit':
            exit()
        while not re.match("^[A-Za-z]$", inp):
            inp = raw_input("That was not a valid letter. Please try again: ")

        #if that letter was already chosen, continue while loop    
        if inp.lower() in guesses:
            print("You have already tried that letter.")
            continue

        #otherwise, loop through word to see if the letter 
        # exists or not
        exists = False    
        for i in xrange(0,len(word)):
            if word[i:i+1] == inp.lower():
                wordBool[i] = True
                exists = True
                if all(j == True for j in wordBool):
                    won = True
                    strikes = 7
                    break
        #if it exists then append it to guesses and move on,
        # otherwise add a strike
        if exists:
            guesses.append(inp.lower())
        else:
            guesses.append(inp.lower())
            strikes += 1

    #display if the player has won or lost
    if won:
        print "You won!"
    else:
        print "You lost!"
        printDead()
    #ask if they want to play again or leave
    pa = raw_input("Play again?(y/n):")
    if pa == 'n':
        playing = False