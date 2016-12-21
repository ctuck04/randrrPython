#from randrrPython import p1ScoreConversion, p2ScoreConversion#something
#import unittest

#class TestMyFunctions(unittest.TestCase):


#from unittest.mock import patch
#from mock import MagicMock

from unittest.mock import patch












#if __name__ == '__main__':
    #unittest.main(exit=False)
    
        
#def scoreUpdate(scoreInput):
        #if scoreInput == '1':
            #global p1BaseScore
            #p1BaseScore += 1
            #p1ScoreConversion(p1BaseScore)
            #print "* <", p1name,"> scores! *\n"
            #resumeAction()
            #if (p1BaseScore >= 4 and p1BaseScore - p2BaseScore >= 2):
                #gameWon()
                #print "** <",p1name,"> wins the game!! **"
                #gameReset()
            #scoreBoard()
            #whoScored()
        #elif scoreInput == '2':
            #global p2BaseScore
            #p2BaseScore += 1
            #p2ScoreConversion(p2BaseScore)
            #print "* <",p2name, "> scores! *\n"
            #resumeAction()
            #if (p2BaseScore >= 4 and p2BaseScore - p1BaseScore >= 2):
                #gameWon()
                #print "** <",p2name,"> wins the game!! **"
                #gameReset()
            #scoreBoard()
            #whoScored()
            
@patch("randrrPython.p1ScoreConversion")
def test_scoreUpdate(mock_p1ScoreConversion):
    scoreInput = '1'
    
    scoreUpdate(scoreInput)
    
    assert_equals(mock_p1ScoreConversion.call_count, 1)
    
@patch("randrrPython.resumeAction")
def test_scoreUpdate(mock_resumeAction):
    scoreInput = '1'
    
    scoreUpdate(scoreInput)
    
    assert_equals(mock_resumeAction.call_count, 1)
    
@patch("randrrPython.scoreBoard")
def test_scoreUpdate(mock_scoreBoard):
    scoreInput = '1'
    
    scoreUpdate(scoreInput)
    
    assert_equals(mock_scoreBoard.call_count, 1)
    
@patch("randrrPython.whoScored")
def test_scoreUpdate(mock_whoScored):
    scoreInput = '1'
    
    scoreUpdate(scoreInput)
    
    assert_equals(mock_whoScored.call_count, 1)



#example test below:

#def evaluate (person1, person2):
    #if person1 in person2['likes']:
        #send_email(person1)
        #send_email(person2)
    #elif person1 in person2['dislikes']:
        #let_down_gently(person1)
    #elif person1 not in person2['likes']
        #and person1 not in person2['dislike']:
        #give_it_time(person1)
        
#@patch("application.send_email")        
#@patch("application.let_down_gently")
#@patch("application.give_it_time")
#def test_person2_dislikes_person1(mock_let_down):
    #person1 = 'Bill'
    #person2 = {
        #'likes': ['Sam', 'Joey'],
        #'dislikes' : ['Bill']
        
    #}
    
    #evaluate[person1, person2]

#with parameters:
    #mock_let_down.assert_called_once_with(person1)
    #assert_equals(mock_give_it_time.call_count, 0)
    #assert_equals(mock_send_email.call_count, 0)
    


    