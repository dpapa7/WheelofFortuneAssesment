from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize
from config import finalRoundTextLoc

import random

players={0:{"roundtotal":250,"gametotal":0,"name":""},
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
# usedLetters = []





def readDictionaryFile():
    global dictionary
    with open ('dictionary.txt', 'r') as f:
        for item in f:
            
            dictionary.append(item.strip())

    
    # Read dictionary file in from dictionary file location
    # Store each word in a list.
      

def readTurnTxtFile():
    global turntext   
    with open ('turntext.txt', 'r') as f:
        turntext = f.read()
    #read in turn intial turn status "message" from file


def readFinalRoundTxtFile():
    global finalroundtext   
    with open ('finalround.txt', 'r') as f:
        finalroundtext = f.read()
    #read in turn intial turn status "message" from file


def readRoundStatusTxtFile():
    global roundstatus
    with open (roundstatusloc, 'r') as f:
        roundstatus = f.read()
    # read the round status  the Config roundstatusloc file location 


def readWheelTxtFile():
    global wheellist
    with open (wheeltextloc, 'r') as f:
        for item in f:
            
            wheellist.append(item.strip())
   # read the Wheel name from input using the Config wheelloc file location 


def getPlayerInfo():
    global players
    for i in players:
        players[i]['name'] = input(f"enter the name of player {i+1}: ")

    # read in player names from command prompt input


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
    

def getWord():
    global dictionary
    roundWord = random.choice(dictionary)
    roundWord = roundWord.lower()
    #choose random word from dictionary
    #make a list of the word with underscores instead of letters.
    roundUnderscoreWord = []
    for i in range(0, len(roundWord)):
        roundUnderscoreWord.append("_")

    return roundWord, roundUnderscoreWord


def wofRoundSetup():
    global players
    global roundWord
    global blankWord

    # Set round total for each player = 0
    for i in players:
        players[i]['roundtotal'] = 0

    # Return the starting player number (random)
    initPlayer = random.randrange(0,3)

    # Use getWord function to retrieve the word and the underscore word (blankWord)
    roundWord , blankWord = getWord()
    return initPlayer


def spinWheel(playerNum):
    global wheellist
    global players
    global vowels

    
    x = random.choice(wheellist)

    if x == "Bankrupt":
        print("You landed on Bankrupt!")
        players[playerNum]['roundtotal'] = 0
        stillinTurn = False

    elif x == "Lose a Turn":
        print("You landed on Lose a Turn!")
        stillinTurn = False
    
    else: 
        print(f"You landed on {x}")
        tempName = players[playerNum]['name']
        z = str(input(f"{tempName} please guess a letter: "))
        a , b = guessletter(z,playerNum)

        if a:
            print(f"This letter appears in the word {b} times")
            print(blankWord)
            print(f"{x} has been added to your round total")
            players[playerNum]['roundtotal'] += int(x)
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
    #I added this
    global roundWord

    tempList = []
    tempList[:0] = roundWord
    
    x = True

    count = 0

    while x == True:
        
        if letter in vowels:
            print("you are not allowed to enter a vowel!")
            letter = str(input("Please enter a letter: "))

        else:   
            if letter in tempList:
                for i in range(len(tempList)):
                    if tempList[i] == letter:
                        blankWord[i] = letter   
                 
                goodGuess = True
                count = roundWord.count(letter)
                print(f"{players[playerNum]['name']} {letter} is in the word!")
    
            else:
                print(f"{players[playerNum]['name']} {letter} is not in the word")
                goodGuess = False
            x = False 
       

    # parameters:  take in a letter guess and player number
    # Change position of found letter in blankWord to the letter instead of underscore 
    # return goodGuess= true if it was a correct guess
    # return count of letters in word. 
    # ensure letter is a consonate.
    
    return goodGuess, count


def buyVowel(playerNum):
    global players
    global vowels

    #i added
    global blankWord
    global roundWord

    templist = []
    templist[:0] = roundWord

    roundbal = players[playerNum]["roundtotal"]
    
    if roundbal >= 250:
        
        y = True
        while y == True:
            templetter = str(input("\nPlease enter a vowel: ")) 
            templetter = templetter.strip().lower()
            
            if templetter in vowels:
                players[playerNum]["roundtotal"] = (roundbal - 250)
                y = False
                if templetter in templist:
                    goodGuess = True
                    print(f"\nGood Guess! {templetter} is in the word!\n")
                    for i in range(len(templist)):
                        if templist[i] == templetter:
                            blankWord[i] = templetter
                        
                    print(blankWord)

                else:
                    print(f"\nSorry {templetter} is not in the word!\n")
                    goodGuess = False
            else:
                print("\nThat was not a vowel! Try again!\n")
                y = True

    else:
        print(f"\nPlayer {playerNum + 1} does not have enough money to buy a vowel")
        goodGuess = True
    # Take in a player number
    # Ensure player has 250 for buying a vowelcost
    # Use guessLetter function to see if the letter is in the file (HOW IS THIS POSSIBLE GUESSLETTER REJECTS VOWELS)
    # Ensure letter is a vowel
    # If letter is in the file let goodGuess = True
    
    return goodGuess      


def guessWord(playerNum):
    global players
    global blankWord
    global roundWord

    templist = []
    templist[:0] = roundWord

    tempWord = str(input("\nGuess the whole word: "))
    tempWord = tempWord.lower()
    
    if tempWord == roundWord:
        print(f"\nCorrect! Congrats player {playerNum+1}!")
        for i in range(len(templist)):
            z = templist[i] 
            blankWord[i] = z
        print(blankWord)
            
    else:
        print(f"\nsorry payer {playerNum+1} your guess was incorect")

    # Take in player number
    # Ask for input of the word and check if it is the same as wordguess
    # Fill in blankList with all letters, instead of underscores if correct 
    # return False ( to indicate the turn will finish)  
    
    return False
    

def wofTurn(playerNum):  
    global roundWord
    global blankWord
    global turntext
    global players

    readRoundStatusTxtFile()
    readWheelTxtFile()

    # take in a player number. 
    # use the string.format method to output your status for the round
    # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update roundtotal 
    
    stillinTurn = True
    while stillinTurn:

        print(turntext.format(nameturn = players[playerNum]["name"], moneyturn = players[playerNum]["roundtotal"]))


        choice = str(input("Please select one of the following\n1. (S)pin the wheel \n2. (B)uy a vowel \n3. (G)uess the word \n\nYour Selection:"))

        # use the string.format method to output your status for the round
        # Get user input S for spin, B for buy a vowel, G for guess the word
                
        if(choice.strip().upper() == "S"):
            stillinTurn = spinWheel(playerNum)
        elif(choice.strip().upper() == "B"):
            stillinTurn = buyVowel(playerNum)
        elif(choice.upper() == "G"):
            stillinTurn = guessWord(playerNum)
        else:
            print("\nNOT A CORRECT OPTION\n")        
    
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.     


def wofRound():
    global players
    global roundWord
    global blankWord
    global roundstatus
    
    initPlayer = wofRoundSetup()
    
    x = "_"

    # if blank word is solved
    round = True
    while round:
        
        if x in blankWord:
            if initPlayer > 2:
                initPlayer = 0

            wofTurn(initPlayer)
            initPlayer += 1

        else:
            
            #push winners roundtotal to gametotal
            initPlayer -= 1
            y = players[initPlayer]["roundtotal"]
            players[initPlayer]["gametotal"] = y
            playername =players[initPlayer]["name"]
           
            print(roundstatus.format(playerName = playername, win = players[initPlayer]["gametotal"]))
            round = False
    

    # Keep doing things in a round until the round is done ( word is solved)
        # While still in the round keep rotating through players
        # Use the wofTurn fuction to dive into each players turn until their turn is done.
    
    # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.

def wofFinalRound():
    global roundWord
    global blankWord
    global finalroundtext
    global finalprize
    winplayer = 0
    amount = finalprize

    roundWord , blankWord = getWord()

    x =[]
        #put all game totals in a list
    for i in players:
        x.append(players[i]["gametotal"])
    
        #find what index player has the highest gametotal
    playerIndex = x.index(max(x)) 

    name = players[playerIndex]["name"]

    print(finalroundtext.format(finalplayername = name, amount = amount))

    
    getWord()
      
    roundwordList = [c for c in roundWord]


    
    
    i = 0
    finallist = ['r', 's', 't','l','n']
    for i in range(0,len(finallist)):
        templet = finallist[i]
        a, b = guessletter(templet, playerIndex)
        if a == True:
            if roundwordList[i] not in vowels:
                blankWord[i] = templet
        
        
        else: 
            blankWord[i] = "_"
    
    # need to do e
    e = 'e'
    if e in roundwordList:
        print(f"{name} e is in the word!")        
        eIndex = roundwordList.index('e')
        blankWord[eIndex] = e

    
    print(f"\n{blankWord}")
        

    for i in range(0,3):
        
        const = False
        while  const == False:  
            finguess = input("Please enter a constonant: ")
            if finguess not in vowels:    
                if finguess in roundwordList:
                    print(f"{finguess} is in the word!")
                    gIndex = roundwordList.index(finguess)
                    blankWord[gIndex] = finguess
                else:
                    print(f"{finguess} is not in the word")
                const = True
            else:
                print(f"{finguess} is not a constonant")
            


    print(blankWord)

    vowelcheck = False
    while vowelcheck == False:
        vowelguess = str(input("Please enter 1 vowel: "))
        if vowelguess in vowels:
            if vowelguess in roundwordList:
                print(f"{vowelguess} is in the word")
                vIndex = roundwordList.index(vowelguess)
                blankWord[vIndex] = vowelguess
                
            else:
                print(f"{vowelguess} is not in the word")
            vowelcheck = True
        else:
            print("You can only enter a vowel! ")
    

    print(f"This is what is left \n{blankWord}")

    
    guessWord(playerIndex)

    if "_" in blankWord:
        print("Better luck nextime! :(")
    
    else:
        gametotal = players[playerIndex]["gametotal"] 

        finalprize = (amount + gametotal)
        pname = players[playerIndex]["name"] 

        print(f"congratulation {pname} you have won Wheel of fortune! \nYour total winnings are {finalprize}")
   

    # Find highest gametotal player.  They are playing.
    # Print out instructions for that player and who the player is.
    # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
    # Use the guessletter function to check for {'R','S','T','L','N','E'}
    # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}

    
    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    # Print out the current blankWord again
    # Remember guessletter should fill in the letters with the positions in blankWord
    # Get user to guess word
    # If they do, add finalprize and gametotal and print out that the player won 


def main():
    gameSetup()    
  
    # i = 2

    for i in range(0,maxrounds):
        if i in [0,1]:
            wofRound()
        else:
            wofFinalRound()

if __name__ == "__main__":
    main()



  
  

