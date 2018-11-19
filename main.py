from random import randint
import ComputerAi
from BoardOperations import BoardOperation

gameBoard = ["none", "none", "none", "none", "none", "none", "none", "none", "none"]



def GameLoop():
    victoryReached = False
    moveCounter = 1
    newBoard = BoardOperation(gameBoard)


    newBoard.DetermineFirstMove()

    while(not victoryReached):
        print("Draw board")

        newBoard.DrawBoardToConsole()

        #Make play game until victory

        if(moveCounter == 10):
            return

        if(newBoard.computerMove):
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