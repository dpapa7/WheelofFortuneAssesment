from sqlalchemy import Integer
from sympy import total_degree
from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize
from config import finalRoundTextLoc

import random

players={0:{"roundtotal":0,"gametotal":0,"name":""},
         1:{"roundtotal":0,"gametotal":0,"name":""},
         2:{"roundtotal":0,"gametotal":0,"name":""},
        }

roundNum = 0
dictionary = []
turntext = ""
wheellist = []
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
roundstatus = ""
finalroundtext = ""


#WORKING (CHANGED LOCATION)
def readDictionaryFile():
    global dictionary
    with open ('dictionary.txt', 'r') as f:
        for item in f:
            
            dictionary.append(item.strip())

    
    # Read dictionary file in from dictionary file location
    # Store each word in a list.
      




#KIND OF WORKING
def readTurnTxtFile():
    global turntext   
    with open ('turntext.txt', 'r') as f:
        turntext = f.read()
    #read in turn intial turn status "message" from file



#SHOULD BE WORKING  
def readFinalRoundTxtFile():
    global finalroundtext   
    with open ('finalround.txt', 'r') as f:
        finalroundtext = f.read()
    #read in turn intial turn status "message" from file



#SHOULD BE WORKING
def readRoundStatusTxtFile():
    global roundstatus
    with open (roundstatusloc, 'r') as f:
        roundstatus = f.read()
    # read the round status  the Config roundstatusloc file location 



#WORKING
def readWheelTxtFile():
    global wheellist
    with open (wheeltextloc, 'r') as f:
        for item in f:
            
            wheellist.append(item.strip())
   # read the Wheel name from input using the Config wheelloc file location 

readWheelTxtFile()
print(wheellist)

#WORKING
def getPlayerInfo():
    global players
    for i in players:
        players[i]['name'] = input(f"enter the name of player {i+1}: ")

    # read in player names from command prompt input


#HAVENT CHANGED
def gameSetup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turntext
    global dictionary
        
    readDictionaryFile()
    readTurnTxtFile()
    readWheelTxtFile()
    getPlayerInfo()
    readRoundStatusTxtFile()
    readFinalRoundTxtFile() 
    
#WORKS    
def getWord():
    global dictionary
    roundWord = random.choice(dictionary)
    #choose random word from dictionary
    #make a list of the word with underscores instead of letters.
    roundUnderscoreWord = []
    for i in range(0, len(roundWord)):
        roundUnderscoreWord.append("_")

    return roundWord, roundUnderscoreWord

#confusing (I think works)
def wofRoundSetup():
    global players
    global roundWord
    global blankWord

    # Set round total for each player = 0
    for i in players:
        players[i]['roundtotal'] = 0

    # Return the starting player number (random)
    initPlayer = random.randrange(0,1,2)

    # Use getWord function to retrieve the word and the underscore word (blankWord)
    roundWord , blankWord = getWord()
    return initPlayer



def spinWheel(playerNum):
    global wheellist
    global players
    global vowels

    
    x = random.choice(wheellist)

    if x == "Bankrupt":
        players[playerNum-1]['roundtotal'] = 0
        stillinTurn = False

    elif x == "Lose a Turn":
        stillinTurn = False
    
    else: 
        tempName = players[playerNum-1]['name']
        input(f"{tempName} please guess a letter: ")

        if letter in word:
            show letters
            players[playerNum - 1]['roundtotal'] = int(x)
            stillinTurn = True

        else:
            stillinTurn = False

        

    # Get random value for wheellist
    # Check for bankrupcy, and take action.
    # Check for loose turn
    # Get amount from wheel if not loose turn or bankruptcy
    # Ask user for letter guess
    # Use guessletter function to see if guess is in word, and return count
    # Change player round total if they guess right.     
    return stillinTurn




def guessletter(letter, playerNum): 
    global players
    global blankWord




    # parameters:  take in a letter guess and player number
    # Change position of found letter in blankWord to the letter instead of underscore 
    # return goodGuess= true if it was a correct guess
    # return count of letters in word. 
    # ensure letter is a consonate.
    
    return goodGuess, count

def buyVowel(playerNum):
    global players
    global vowels
    
    # Take in a player number
    # Ensure player has 250 for buying a vowelcost
    # Use guessLetter function to see if the letter is in the file
    # Ensure letter is a vowel
    # If letter is in the file let goodGuess = True
    
    return goodGuess      
        
def guessWord(playerNum):
    global players
    global blankWord
    global roundWord
    
    # Take in player number
    # Ask for input of the word and check if it is the same as wordguess
    # Fill in blankList with all letters, instead of underscores if correct 
    # return False ( to indicate the turn will finish)  
    
    return False
    
    
# def wofTurn(playerNum):  
#     global roundWord
#     global blankWord
#     global turntext
#     global players

#     # take in a player number. 
#     # use the string.format method to output your status for the round
#     # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
#     # Keep doing all turn activity for a player until they guess wrong
#     # Do all turn related activity including update roundtotal 
    
#     stillinTurn = True
#     while stillinTurn:
        
#         # use the string.format method to output your status for the round
#         # Get user input S for spin, B for buy a vowel, G for guess the word
                
#         if(choice.strip().upper() == "S"):
#             stillinTurn = spinWheel(playerNum)
#         elif(choice.strip().upper() == "B"):
#             stillinTurn = buyVowel(playerNum)
#         elif(choice.upper() == "G"):
#             stillinTurn = guessWord(playerNum)
#         else:
#             print("Not a correct option")        
    
#     # Check to see if the word is solved, and return false if it is,
#     # Or otherwise break the while loop of the turn.     


# def wofRound():
#     global players
#     global roundWord
#     global blankWord
#     global roundstatus
#     initPlayer = wofRoundSetup()
    
#     # Keep doing things in a round until the round is done ( word is solved)
#         # While still in the round keep rotating through players
#         # Use the wofTurn fuction to dive into each players turn until their turn is done.
    
#     # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.

# def wofFinalRound():
#     global roundWord
#     global blankWord
#     global finalroundtext
#     winplayer = 0
#     amount = 0
    
#     # Find highest gametotal player.  They are playing.
#     # Print out instructions for that player and who the player is.
#     # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
#     # Use the guessletter function to check for {'R','S','T','L','N','E'}
#     # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
#     # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
#     # Print out the current blankWord again
#     # Remember guessletter should fill in the letters with the positions in blankWord
#     # Get user to guess word
#     # If they do, add finalprize and gametotal and print out that the player won 


# def main():
#     gameSetup()    

#     for i in range(0,maxrounds):
#         if i in [0,1]:
#             wofRound()
#         else:
#             wofFinalRound()

# if __name__ == "__main__":
#     main()
    
    
