import random

# open the logfile

logFile = open("logfile_21071899.txt", "a")

# converting box number to row and column. DICTIONARY
correspondingMoveRC = {
        0: [1,1], 1: [1,2], 2: [1,3],
        3: [2,1], 4: [2,2], 5: [2,3],
        6: [3,1], 7: [3,2], 8: [3,3] }

playerTurns = 5

# layout of the tictactoe board

theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            
def printBoard():
    print(theBoard[0] + '|' + theBoard[1] + '|' + theBoard[2])
    print('-+-+-')
    print(theBoard[3] + '|' + theBoard[4] + '|' + theBoard[5])
    print('-+-+-')
    print(theBoard[6] + '|' + theBoard[7] + '|' + theBoard[8])

def checkBoardWin(moves, turn):   
    # At least 5 moves has to be made for someone to win
    if moves >= 5:
        
        if theBoard[6] == theBoard[7] == theBoard[8] != ' ': # across the top
            printBoard()
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            return True
                
        elif theBoard[3] == theBoard[4] == theBoard[5] != ' ': # across the middle
            printBoard()
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            return True
            
        elif theBoard[0] == theBoard[1] == theBoard[2] != ' ': # across the bottom
            printBoard()
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            return True
            
        elif theBoard[0] == theBoard[3] == theBoard[6] != ' ': # down the left side
            printBoard()
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            return True
            
        elif theBoard[1] == theBoard[4] == theBoard[7] != ' ': # down the middle
            printBoard()
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            return True
            
        elif theBoard[2] == theBoard[5] == theBoard[8] != ' ': # down the right side
            printBoard()
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            return True
             
        elif theBoard[6] == theBoard[4] == theBoard[2] != ' ': # diagonal
            printBoard()
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            return True
            
        elif theBoard[0] == theBoard[4] == theBoard[8] != ' ': # diagonal
            printBoard()
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            return True
        
        return False
    else:
        return False
    
# define the game

def game():
    moves = 0
    gameEnd = False
    
    for i in range(playerTurns):
        printBoard()

        turn = "Player"
        # get player input
        
        while True:
            print("It's your turn, " + turn + ". Move to which place?")
            playerMove = int(input()) - 1
            
            if theBoard[playerMove] == ' ':
                theBoard[playerMove] = "X"
                moves += 1

    # converting tictactoe  box number to row and column into logfile record
            
                rc = correspondingMoveRC[playerMove]
                logMsg = f"{moves}, P, {rc[0]}, {rc[1]}, X\n"
                logFile.write(logMsg)
                break
            
            print("You gave a wrong input! Please try again.\n")

        # if there is a Win the game will End
        if(checkBoardWin(moves, turn)):
            gameEnd = True
            break

        # computer turn
        if moves < 9:
            turn = "Computer"
            print('\nIts ' + turn + ' turn to move\n')
            while True:
                computerMove = random.randint(0,8)

                if theBoard[computerMove] == ' ':
                    theBoard[computerMove] = "O"
                    moves += 1

                    rc = correspondingMoveRC[computerMove]
                    logMsg = f"{moves}, C, {rc[0]}, {rc[1]}, O\n"
                    logFile.write(logMsg)
                    break
            
            if(checkBoardWin(moves, turn)):
                gameEnd = True
                break
# if by the end of the whole game no one has a win, it's a tie

    if not gameEnd:
        printBoard()
        print("\nGame Over.\n")                
        print("It's a Tie!")

# a loop for the entire game 

while True:
    game()
    logFile.write("========================== NEW ROUND ==========================\n")
    
    # once games ends, player will be asked to replay game
    
    print("Replay the game? Y/N")

    if(input() != "Y"):
        break

    # Reset game variables
    theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# spacing the logfile records after player sihes not to replay
logFile.write("========================== NEW MATCH ENTRY ========================== \n")
logFile.close()
