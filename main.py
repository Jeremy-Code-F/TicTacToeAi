from random import randint
import ComputerAi

gameBoard = ["none", "none", "none", "none", "none", "none", "none", "none", "none"]

def DrawBoardToConsole():
    print('\n')
    print('\n')
    
    x = 0
    for thing in gameBoard:
        if(x % 3 == 0):
            print()
        print(thing, end="\t")
        x = x + 1

def GameLoop():
    victoryReached = False
    firstMoveIsUser = False
    userMove = False
    computerMove = False
    moveCounter = 1

    coinFlip = randint(0, 1)

    if(coinFlip == 1):
        firstMoveIsUser = True
        userMove = True
        computerMove = False
    else:
        firstMoveIsUser = False
        computerMove = True
    
    while(not victoryReached):

        DrawBoardToConsole()

        if(moveCounter == 10):
            return

        if(computerMove):
            print("This is the computers turn:")
            ComputerAi.MakeMoveTest(gameBoard, moveCounter)
            computerMove = False
            userMove = True
            moveCounter = moveCounter + 1
            continue
        else:
            finishedWithTurn = False

            while(not finishedWithTurn):
                currentMove = input("Enter 1-9 for your move")
                if(gameBoard[(int(currentMove) - 1)] == "none"):
                    gameBoard[(int(currentMove) - 1)] = "x"
                    computerMove = True
                    userMove = False
                    finishedWithTurn = True
                    moveCounter = moveCounter + 1
                else:
                    print("Space already taken play another square")
            continue
            
            


        
    
        


if __name__ == '__main__':
    GameLoop()
    x = 0
    print('\n')
    print('\n')
    for thing in gameBoard:
        
        if(x % 3 == 0):
            print()
        print(thing, end="\t")
        x = x + 1