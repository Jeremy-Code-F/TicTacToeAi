from random import randint

def CheckSpaces(winConditionSpaces, boardSpaces):


    for row in winConditionSpaces:
        print()
        #print("Checking : " + str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
        if( (boardSpaces[row[0]] == 'x' and boardSpaces[row[1]] == 'x' and boardSpaces[row[2]] == 'x') or (boardSpaces[row[0]] == 'o' and boardSpaces[row[1]] == 'o' and boardSpaces[row[2]] == 'o') ):
            return True
    return False
            

class BoardOperation:


    def __init__(self, board):
        self.gameBoard = board
        self.userMove = False
        self.computerMove = False

    

 #win conditions - [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7] - non-zero based
    def CheckForWinConditions(self):
        winConditions = [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
        #print("Checking to see if anyone has won")
        victoryReached = CheckSpaces(winConditions, self.gameBoard)
        #print("Victory reached: " + str(victoryReached))
         
        return victoryReached

    



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
