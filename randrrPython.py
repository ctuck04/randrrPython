import subprocess as sp
import time
import math

##########################################################################################

# This is essentially the entry point. Both players enter their names.
# Entering an empty String is considered invalid input.

p1name = raw_input("\n\nEnter Player 1 name: ")
while p1name == "":
    print("Please enter a valid name!")
    p1name = raw_input("Player 1: ")

p2name = raw_input("Enter Player 2 name: ")
while p2name == "":
    print("Please enter a valid name!")
    p2name = raw_input("Player 2: ")
    
p1BaseScore = 0
p2BaseScore = 0
p1WordScore = "Love"
p2WordScore = "Love"
p1AdjScore = 0
p2AdjScore = 0

##########################################################################################

# This where the user enters who scored in the present game. If the user presses
# anything besides the '1' or '2' key, it simply re-prompts the user.

def whoScored():
    print("\n\nWho scored?\n")
    print ("For <",p1name,"> press '1'\nFor <",p2name,"> press '2'\n")
    scoreInput = raw_input("")
    tmp = sp.call('clear',shell=True)
    while scoreInput not in {'1', '2'}:
        scoreBoard()
        whoScored()
    while scoreInput in {'1', '2'}:
        scoreUpdate(scoreInput)

##########################################################################################

# This function takes the user input, updates the players' scores, and
# converts the players' scores, as well as checks for a game winning condition.

def scoreUpdate(scoreInput):
        if scoreInput == '1':
            global p1BaseScore
            p1BaseScore += 1
            p1ScoreConversion(p1BaseScore)
            print ("* <", p1name,"> scores! *\n")
            resumeAction()
            if (p1BaseScore >= 4 and p1BaseScore - p2BaseScore >= 2):
                gameWon()
                print ("** <",p1name,"> wins the game!! **")
                gameReset()
            scoreBoard()
            whoScored()
        elif scoreInput == '2':
            global p2BaseScore
            p2BaseScore += 1
            p2ScoreConversion(p2BaseScore)
            print ("* <",p2name, "> scores! *\n")
            resumeAction()
            if (p2BaseScore >= 4 and p2BaseScore - p1BaseScore >= 2):
                gameWon()
                print ("** <",p2name,"> wins the game!! **")
                gameReset()
            scoreBoard()
            whoScored()

##########################################################################################        

# Once a game has been won, this function resets the screen. It doesn't actually
# handle resetting the scores.

def gameWon():
    tmp = sp.call('clear',shell=True)
    time.sleep(2)
    print ("**********")
    print ("*VICTORY!*")
    print ("**********")
    time.sleep(2)
    tmp = sp.call('clear',shell=True)

##########################################################################################    

# This function decides which version of the scoreboard the user sees.

def scoreBoard():

    scoreVersion = 0

    if p1BaseScore == 0 and p2BaseScore == 0:
         wordBoard(scoreVersion)
    elif p1BaseScore > 0 and p2BaseScore == 0:
        scoreVersion = 1
        wordBoard(scoreVersion)
    elif p1BaseScore == 0 and p2BaseScore > 0:
        scoreVersion = 2
        wordBoard(scoreVersion)
    elif (
            p1BaseScore > 0 and p1BaseScore <= 3 and 
            p2BaseScore > 0 and p2BaseScore <= 3 and 
            abs(p1BaseScore - p2BaseScore) >= 1
          ):
        scoreVersion = 3
        wordBoard(scoreVersion)
    elif (
            p1BaseScore < 3 and p2BaseScore < 3 and 
            p1BaseScore > 0 and p2BaseScore > 0
          ):
        scoreVersion = 3
        wordBoard(scoreVersion)
    elif (
            (p1BaseScore >= 3 or p2BaseScore >= 3) and 
             p1BaseScore - p2BaseScore == 0
          ):
        scoreVersion = 4
        wordBoard(scoreVersion)
    elif ( 
            p1BaseScore >= 3 and p2BaseScore >= 3 
            and p1BaseScore > p2BaseScore
          ):
        scoreVersion = 5
        wordBoard(scoreVersion)
    elif ( 
            p1BaseScore >= 3 and p2BaseScore >= 3 
            and p1BaseScore < p2BaseScore
          ):
        scoreVersion = 6
        wordBoard(scoreVersion)

##########################################################################################    

# This function takes a parameter from scoreBoard() and prints out the appropriate
# scoreboard.

def wordBoard(scoreVersion):
    
    global p1WordScore
    global p2WordScore

    if scoreVersion == 0:
        print ("<",p1name,">: ", p1WordScore, "\t<",p2name,">: ", p2WordScore,"\n")
    elif scoreVersion == 1:
        print ("<",p1name,">: ", p1AdjScore, "\t<",p2name,">: ", p2WordScore,"\n")
    elif scoreVersion == 2:
        print ("<",p1name,">: ", p1WordScore, "\t<",p2name,">: ", p2AdjScore,"\n")
    elif scoreVersion == 3:
        print ("<",p1name,">: ", p1AdjScore, "\t<",p2name,">: ", p2AdjScore,"\n")
    elif scoreVersion == 4:
        print ("DEUCE")
    elif scoreVersion == 5:
        print ("Advantage: ",p1name)
    elif scoreVersion == 6:
        print ("Advantage: ",p2name)

##########################################################################################

# The next two functions convert the points of their respective players and convert them
# into tennis' odd scoring system.

def p1ScoreConversion(baseScore):
    
    global p1AdjScore
    
    if baseScore == 1:
        p1AdjScore = 15
    elif baseScore == 2:
        p1AdjScore = 30
    elif baseScore == 3:
        p1AdjScore = 40
    elif  baseScore == 4:
        p1AdjScore = 50

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
 
def p2ScoreConversion(baseScore):
    
    global p2AdjScore
    
    if baseScore == 1:
        p2AdjScore = 15
    elif baseScore == 2:
        p2AdjScore = 30
    elif baseScore == 3:
        p2AdjScore = 40
    elif  baseScore == 4:
        p2AdjScore = 50
    
##########################################################################################

# This function resets the player scores.

def gameReset():
    
    time.sleep(2)
    tmp = sp.call('clear',shell=True)
    
    global p1BaseScore
    global p2BaseScore
    
    p1BaseScore = 0
    p2BaseScore = 0
    
    whoScored()

##########################################################################################    

# This function keeps things moving after a player scores.

def resumeAction():
    time.sleep(2)
    tmp = sp.call('clear',shell=True)
    time.sleep(1)
    
##########################################################################################
    
# The below code executes after the players have entered their names.

tmp = sp.call('clear',shell=True)
time.sleep(2)

scoreBoard()
whoScored()   

