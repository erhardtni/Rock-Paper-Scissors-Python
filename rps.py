import random
import time

#This is a simple rock paper scissors game.

print("-------------------- Let's play a game of Rock, Paper, Scissors --------------------")
time.sleep(2)

def main():
    ValidInput = False
    while not ValidInput:
        try:
            print('\n')
            hand = ['rock', 'paper', 'scissors']
            playerOp = input('Rock, paper, scissors shoot: ')
            computerOp = random.choice(hand)
            
            if(playerOp == 'rock' or playerOp == 'paper' or playerOp == 'scissors'):
                print('\n')
            else:
                print('\n')
                print('Invalid input! You can only select rock, paper, or scissors, you dingus')
                return main()
            
#We do this because there are only 3 items you can play in rock paper scissors. Pretty self explanatory.
               
            print('You chose ' + playerOp)
            time.sleep(2)
            print('\n')
            print('Computer chose ' + computerOp)
            time.sleep(2)
            print('\n')
            
#The following if and elif statements correspond to the rules of rock, paper, scissors. Rock beats scissors, scissors beats paper, and paper beats rock. I always thought it was kind of weird that a piece of paper could smite a rock, but that's just my opinion I guess.
            
            if((playerOp == 'rock' and computerOp == 'paper') or (playerOp == 'scissors' and computerOp == 'rock') or (playerOp == 'paper' and computerOp == 'scissors')):
                print('You lose! Better luck next time ¯\_(ツ)_/¯')
            elif((playerOp == 'rock' and computerOp == 'scissors') or (playerOp == 'scissors' and computerOp == 'paper') or (playerOp == 'paper' and computerOp == 'rock')):
                print('Winner winner chicken dinner')
            elif((playerOp == 'rock' and computerOp == 'rock') or (playerOp == 'paper' and computerOp == 'paper') or (playerOp == 'scissors' and computerOp == 'scissors')):
                print('You tied with the computer, you might want to play best 2 out of 3...')
            else:
                print('Invalid input')
            
            ValidInput = True
            
        except:
            print("unknown error")    
    
#This next function is a means of making this rock, paper, scissors game playable as many times as the player wants without having to exit and execute the script again for each time they want to play.
    
    def playagain():
        again = input('Would you like to play again? (y/n) ')
        if(again == 'n'):
            print('\n')
            print("Thank you for playing rock, paper, scissors. Goodbye!")
        elif(again == 'y'):
            #callback main function
            return main()
        else:
            #callback the playagain function and clarify 
            print('\n')
            print("Invalid input! Please enter y for yes or n for no. ")
            print('\n')
            return playagain()
                  
    print('\n\n')              
    playagain()
    
main()   