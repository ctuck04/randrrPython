import subprocess as sp
import time
import math

##########################################################################################

# This is essentially the entry point. Both players enter their names.
# Entering an empty String is considered invalid input.

def entryPoint():

    global p1name
    global p2name

    p1name = input("\n\nEnter Player 1 name: ")
    while p1name == "":
        print("Please enter a valid name!")
        p1name = input("Player 1: ")

    p2name = input("Enter Player 2 name: ")
    while p2name == "":
        print("Please enter a valid name!")
        p2name = input("Player 2: ")
    
    global p1BaseScore
    global p2BaseScore 
    global p1WordScore 
    global p2WordScore 
    global p1AdjScore 
    global p2AdjScore 
    global p1SetScore 
    global p2SetScore 
    global p1MatchScore 
    global p2MatchScore
    
    p1BaseScore = 0
    p2BaseScore = 0
    p1WordScore = "Love"
    p2WordScore = "Love"
    p1AdjScore = 0
    p2AdjScore = 0
    p1SetScore = 0
    p2SetScore = 0
    p1MatchScore = 0
    p2MatchScore = 0

##########################################################################################

# This where the user enters who scored in the present game. If the user presses
# anything besides the '1' or '2' key, it simply re-prompts the user.

def whoScored():
    print("\n\nWho scored?\n")
    print ("For <",p1name,"> press '1'\nFor <",p2name,"> press '2'\n\n")
    print("Press '4' to quit...")
    scoreInput = input("")
    tmp = sp.call('clear',shell=True)
    while scoreInput not in {'1', '2', '4'}:
        scoreBoard()
        whoScored()
    while scoreInput in {'1', '2', '4'}:
        if(scoreInput == '4'):
            exit()
        scoreUpdate(scoreInput)

##########################################################################################

# This function takes the user input, updates the players' scores, and
# converts the players' scores, as well as checks for game, set, and match 
# winning conditions.

def scoreUpdate(scoreInput):
        if scoreInput == '1':
            global p1BaseScore
            p1BaseScore += 1
            p1ScoreConversion(p1BaseScore)
            print ("* <", p1name,"> scores! *\n")
            resumeAction()
            if (p1BaseScore >= 4 and p1BaseScore - p2BaseScore >= 2):
                global p1SetScore
                p1SetScore += 1   
                gameWon()
                if (p1SetScore >= 6 and p1SetScore - p2SetScore >= 2):
                    setWon()
                    global p1MatchScore
                    p1MatchScore+=1
                    matchCheck()
                    setReset()     
                elif (p1SetScore == 7 and p2SetScore == 6):
                    setWon()
                    global p1MatchScore
                    p1MatchScore+=1
                    matchCheck()
                    setReset()
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
                global p2SetScore
                p2SetScore += 1
                gameWon()
                if (p2SetScore >= 6 and p2SetScore - p1SetScore >= 2):
                    setWon()
                    global p2MatchScore
                    p2MatchScore+=1
                    matchCheck()
                    setReset()
                elif (p2SetScore == 7 and p1SetScore == 6):
                    setWon()
                    global p2MatchScore
                    p2MatchScore+=1
                    matchCheck()
                    setReset()
                gameReset()
            scoreBoard()
            whoScored()

##########################################################################################        

# Once a game has been won, this function resets the screen. It doesn't actually
# handle resetting the scores.

def gameWon():
    
    if (p1BaseScore > p2BaseScore):
        tmp = sp.call('clear',shell=True)
        time.sleep(1)
        print ("**********")
        print ("*VICTORY!*")
        print ("**********\n\n")
        print ("** <",p1name,"> wins the game!! **")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)   
    
    elif (p2BaseScore > p1BaseScore):
        tmp = sp.call('clear',shell=True)
        time.sleep(1)
        print ("**********")
        print ("*VICTORY!*")
        print ("**********\n\n")
        print ("** <",p2name,"> wins the game!! **")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        
##########################################################################################

# This is function is similar to the above function. The only difference is that
# it handles notifying a player that they have won the set.

def setWon():
       
    global p1BaseScore
    global p2BaseScore
    
    p1BaseScore = 0
    p2BaseScore = 0
    
    if (p1SetScore > p2SetScore):
        tmp = sp.call('clear',shell=True)
        time.sleep(1)
        print ("** <",p1name,"> ALSO wins the set!! **")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
        
    elif (p2SetScore > p1SetScore):
        tmp = sp.call('clear',shell=True)
        time.sleep(1)
        print ("** <",p2name,"> ALSO wins the set!! **")
        time.sleep(1)
        tmp = sp.call('clear',shell=True)
    
##########################################################################################

# This function checks for a match winning condition.

def matchCheck():
    if (p1MatchScore == 3 and p2MatchScore <= 2):
        matchWon()
    elif (p2MatchScore == 3 and p1MatchScore <= 2):
        matchWon()


##########################################################################################

# This function checks to see which player won and prints accordingly.

def matchWon():

    
    if (p1MatchScore > p2MatchScore):
        print(p1name, " WINS!!")
        reset()
    elif (p1MatchScore < p2MatchScore):
        print(p2name, " WINS!!")
        reset()
         
##########################################################################################

# This function resets the game or allows the player to quit.

def reset():
    time.sleep(1)
    tmp = sp.call('clear',shell=True)
    playAgainOrNah = input("Play again? ")
    print ("\n\nPress '3' to play again...\n")
    print ("Press '4' to quit...")
    while playAgainOrNah not in {'3', '4'}:
        reset()
    while playAgainOrNah in {'3', '4'}:
        if (playAgainOrNah == '3'):
            entryPoint()
        elif(playAgainOrNah == '4'):
            exit()
            
        


    

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
        setBoard()
        print ("<",p1name,">: ", p1WordScore, "\t<",p2name,">: ", p2WordScore,"\n")
    elif scoreVersion == 1:
        setBoard()
        print ("<",p1name,">: ", p1AdjScore, "\t<",p2name,">: ", p2WordScore,"\n")
    elif scoreVersion == 2:
        setBoard()
        print ("<",p1name,">: ", p1WordScore, "\t<",p2name,">: ", p2AdjScore,"\n")
    elif scoreVersion == 3:
        setBoard()
        print ("<",p1name,">: ", p1AdjScore, "\t<",p2name,">: ", p2AdjScore,"\n")
    elif scoreVersion == 4:
        setBoard()
        print ("DEUCE")
    elif scoreVersion == 5:
        setBoard()
        print ("Advantage: ",p1name)
    elif scoreVersion == 6:
        setBoard()
        print ("Advantage: ",p2name)
        
##########################################################################################

# This function simply shows the set score.

def setBoard():
    print("Match Score: ", p1MatchScore," - ",p2MatchScore,"\n")
    print("Set Score:   ", p1SetScore, " - ",p2SetScore,"\n")
    

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
    
    time.sleep(1)
    tmp = sp.call('clear',shell=True)
    
    global p1BaseScore
    global p2BaseScore
    
    p1BaseScore = 0
    p2BaseScore = 0
    
    scoreBoard()
    whoScored()

##########################################################################################    

# This function resets the set scores.

def setReset():
    
    time.sleep(1)
    tmp = sp.call('clear',shell=True)
    
    global p1SetScore
    global p2SetScore
    
    p1SetScore = 0
    p2SetScore = 0
    
    scoreBoard()
    whoScored()


##########################################################################################    

# This function keeps things moving after a player scores.

def resumeAction():
    time.sleep(1)
    tmp = sp.call('clear',shell=True)
    time.sleep(1)
    
##########################################################################################
    
# The below code executes after the players have entered their names.

entryPoint()

tmp = sp.call('clear',shell=True)
time.sleep(1)

scoreBoard()
whoScored()   

