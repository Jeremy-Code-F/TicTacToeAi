from random import randint

class BoardOperation:


    def __init__(self, board):
        self.gameBoard = board
        self.userMove = False
        self.computerMove = False

    def CheckForWinConditions(self, board):
        print("Checking to see if anyone had won")


    def GetWhosTurn(self):
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


        return True

    def DrawBoardToConsole(self):
        print('\n')
        print('\n')
    
        x = 0
        for thing in self.gameBoard:
            if(x % 3 == 0):
                print()
            print(thing, end="\t")
            x = x + 1


    def DetermineFirstMove(self):
        coinFlip = randint(0, 1)

        if(coinFlip == 1):
            self.userMove = True
            self.computerMove = False
        else:
            self.userMove = False
            self.computerMove = True
