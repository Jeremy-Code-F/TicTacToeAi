from random import randint


def MakeFirstMove(board):
    print("Computer's first move")
    board[4] = "o"
    return


def MakeMoveTest(board, moveNumber):
    finishedWithMove = False

    while not finishedWithMove:

        if moveNumber == 1:
            MakeFirstMove(board)
            finishedWithMove = True
        else:


            move = randint(0, 8)

            if(board[int(move)] != "none"):
                continue
            else:
                board[int(move)] = "o"
                finishedWithMove = True
                


    return

        

    