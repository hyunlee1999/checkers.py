# -*- coding: utf-8 -*-
"""

@author: Hyun
"""

board = [[1,2,3,4,5,6,7,8], [11,12,13,14,15,16,17,18], [21,22,23,24,25,26,27,28], [31,32,33,34,35,36,37,38], [41,42,43,44,45,46,47,48], [51,52,53,54,55,56,57,58], [61,62,63,64,65,66,67,68], [71,72,73,74,75,76,77,78]]


def printBoard(board): #Prints out board with input of board
    for row in board:
        for cell in row:
            if isinstance (cell, str) == True:
                print (cell, "  ", end="")
            elif cell > 10:
                print (cell, " ", end="")
            else:
                print (cell, "  ", end="")
        print()
    print()
    
def startingBoard(board): #Sets up the Initial Board
    for row in board:
        rowIndex = board.index(row)
        if rowIndex == 0 or rowIndex == 2:
            for cell in row:
                if cell%2 == 0:
                    row[row.index(cell)] = "o"
            board[rowIndex] = row
        if rowIndex == 1:
            for cell in row:
                if cell%2 == 1:
                    row[row.index(cell)] = "o"
            board[rowIndex] = row
        if rowIndex == 6:
            for cell in row:
                if cell%2 == 0:
                    row[row.index(cell)] = "x"
            board[rowIndex] = row
        if rowIndex == 5 or rowIndex == 7:
            for cell in row:
                if cell%2 == 1:
                    row[row.index(cell)] = "x"
            board[rowIndex] = row
    return board
        

def choosingPiece(): #First Player Chooses a Piece
    global player
    player = str(input("Do you want to be o or x? "))
    if player != "o" and player != "x":
        print("Not Valid Input")
        choosingPiece()
    return player
    
def otherPlayerPiece(player): #Sets other persons piece
    if player == "o":
        otherPlayer = "x"
    else:
        otherPlayer = "o"
    return otherPlayer
     
def initialValidPositionList (board, initialPosition): ##New Function
    playerPiece = findPiece (board, initialPosition)
    
    ##Initial Valid Positions for Unkinged Pieces
    if playerPiece == "o":  
        validPositions = [initialPosition + 11, initialPosition + 9]
    elif playerPiece == "x":
        validPositions = [initialPosition - 11, initialPosition - 9]
        
    #Updated Valid Positions for Kinged Pieces
        
    if playerPiece == "O" or playerPiece == "X":
        validPositions = [initialPosition + 11, initialPosition + 9, initialPosition - 11, initialPosition - 9]
    return validPositions

def playerAndOpponentPieces (playerPiece):
    if playerPiece == "o" or playerPiece == "O":
        opponentPiece = "x"
        opponentKingPiece = "X"
        playerPiece = "o"
        playerKingPiece = "O"
    else: 
        opponentPiece = "o"
        opponentKingPiece = "O"
        playerPiece = "x"
        playerKingPiece = "X"
    return (playerPiece, playerKingPiece, opponentPiece, opponentKingPiece)



def updateValidPosition (board, initialPosition, validPositions):
    global skippingPositions
    
    #Part1 Setting Up Variables and Giving them Value. Also making an empty updated valid positions list.
    
    updatedValidPositions = []
    skippingPositions = []
    initialPiece = findPiece (board, initialPosition)
    pieces = playerAndOpponentPieces(initialPiece)
    playerPiece = pieces[0]
    playerKingPiece = pieces[1]
    opponentPiece = pieces[2]
    opponentKingPiece = pieces[3]
    
    #Part2 Taking the input of initial valid position and appending valid positions.
    #Valid positions may vary. If there is an opponent piece in the valid position, it looks
    #to the final position, and if it is empty, it appends to updatedvalidpositions.
    #Skipping position has 2 elements. First element is the skipped position and the 2nd is final position
    #This helps with 2 skipping positions to determine which.
    
    for position in validPositions:
        if findPiece(board, position) == opponentPiece or findPiece(board, position) == opponentKingPiece:
            tempValidPosition = jumpingPosition(initialPosition, position)
            if type(findPiece(board, tempValidPosition)) == int:
                updatedValidPositions.append(tempValidPosition)
                skippingPositions.append((position,tempValidPosition))
        elif type(findPiece(board, position)) == int:
            updatedValidPositions.append(position)
    return updatedValidPositions
            
    
def jumpingPosition (initialPosition, skippedPosition):
    #Given Initial Position of the Piece and the position
    #and the position that it is skipping, it returns the final position
    difference = skippedPosition - initialPosition
    return skippedPosition + difference



def canDoubleJump (board, moveCount, initialPosition, validPosition):  #New Function
    playerPiece = findPiece (board, initialPosition)
    if playerPiece == "o" or playerPiece == "O":
        opponentPiece = "x"
        opponentKingPiece = "X"
        playerKingPiece = "O"
        
    if playerPiece == "x" or playerPiece =="X":
        playerKingPiece ="X"
        opponentPiece = "o"
        opponentKingPiece = "O"
    
    for position in validPosition:
        if opponentPiece == findPiece (board, position) or opponentKingPiece == findPiece (board, position):
            temp = jumpingPosition (initialPosition, position)
            if type(findPiece(board, temp)) == int:
                return True
    return False

        

def movePiece (board, moveCount, player1, player2, initialPosition = 0, validFinalPositions = []): 
    #InitialPosition = 0 is a placeholder for skipping
    #ValidFinalPosition is needed for skipping. If it is empty, then you can go to any valid position.
    #else, you have to move to the valid final position
    
    #First Part -- Giving Values to Variables
    if moveCount % 2 == 0:
        playerPiece = player1
    else:
        playerPiece = player2
    
    if playerPiece == "o":
        playerKingPiece = "O"
    if playerPiece == "x":
        playerKingPiece = "X"
     
    if initialPosition == 0: 
        initialPosition = int(input("What piece (position) do you want to move? "))
    
        
    
    #Second Part -- Making Sure that the player selected a valid piece.
    
    while findPiece(board, initialPosition) != playerPiece and findPiece(board, initialPosition) != playerKingPiece:  #Checks if a player piece is on the selected cell
        initialPosition = int(input("You've selected an invalid piece. Please select again " ))
        
    while onBoard(initialPosition) == False:
        initialPosition = int(input("You've selected an invalid piece. Please select again " ))        
        

    #Third Part -- Making Sure that the final position is valid
    finalPosition = int(input("Where do you want to place the piece? "))
    
    
    
    
    if validFinalPositions != []:
        while finalPosition not in validFinalPositions:
            finalPosition = int(input("This is not a valid move. Please try again ")) 
            
    
    
    while onBoard(finalPosition) == False:
        finalPosition = int(input("You've selected an invalid piece. Please select again " ))
        
    initialPiece = findPiece(board, initialPosition)
        
    if validMove (board, initialPiece, initialPosition, finalPosition) == False:
        print("This is not a valid move. Try again")
        movePiece (board, moveCount, player1, player2) #Recalls movePiece Function until validMove is true
        
        
    #Fourth Part -- The Pieces is being moved. It replaces the inital position of the piece as a number
    #then, it moves the piece to the original place
    
    else:
        
        #Fourth Part 1st part --> This is for unkinged Pieces
        
        if findPiece(board, initialPosition) == playerPiece:
            temp = findRowCell (board, finalPosition)
            finalRow = (finalPosition//10)
            finalCell = (finalPosition%10) - 1
            board[temp[0]][temp[1]] = playerPiece
            temp = findRowCell (board, initialPosition)
            board[temp[0]][temp[1]] = initialPosition
            
            if isAtEnd (playerPiece, finalPosition) == True:  #"King's the piece if it reaches the end
                changePiece (playerPiece, finalPosition)
                
        #Fourth Part 2nd part --> This is for Kinged Pieces. If initial position is kinged, then final position is kinged.
            

        elif findPiece(board, initialPosition) == playerKingPiece:
            temp = findRowCell (board, finalPosition)
            temp1 = findRowCell (board, initialPosition)
            finalRow = (finalPosition//10)
            finalCell = (finalPosition%10) - 1
            board[temp[0]][temp[1]] = playerKingPiece
            board[temp1[0]][temp1[1]] = initialPosition


        if -15 < finalPosition - initialPosition < 15: #Don't do anything if nothing is being skpped
            return finalPosition 
            
        else: #Need to replace skipped position with the value. ie removing the skipped piece
            
            #Skipping Position list a list of tuples of 2 elements: (skippedposition, finalposition)
            for skippingPosition in skippingPositions:
                if skippingPosition[1] == finalPosition:
                    temp = findRowCell (board, skippingPosition[0])
                    board[temp[0]][temp[1]] = skippingPosition[0]
            
            validPositions = initialValidPositionList(board, finalPosition)
            
            response = 1
            while canDoubleJump(board, moveCount, finalPosition, validPositions) == True and response == 1:
                printBoard (board)
                response = int(input("Type in 1 if you want to double jump, if not, type in 0 "))
                while response != 0 and response != 1:
                    print ("you've selected a wrong number")
                    response = int(input("Type in 1 if you want to double jump, if not, type in 0 "))
        
                if response == 1:
                    validFinalPositions = [] #Creates a valid Final Position for jumping. Because you can't just move, you have to skip.
                
                
                    initialFinalPositions = initialValidPositionList (board, finalPosition) #Initial Final Position
                    updatedFinalPositions = updateValidPosition (board, finalPosition, initialFinalPositions) #Updated Final Position
                    for updatedFinalPosition in updatedFinalPositions:
                    #This function finds updatedfinalPosition that is not in intial valid postion.
                    #If not, this means that the value is skipped.
                        if updatedFinalPosition not in initialFinalPositions:
                            validFinalPositions.append(updatedFinalPosition)
                    finalPosition = movePiece (board, moveCount, player1, player2, finalPosition, validFinalPositions)
            return finalPosition
            
            
            
def findPiece (board, position):
    if onBoard(position) == True:
        row = position//10
        cell = position%10 - 1
        return board[row][cell]
    else:
        return False
    
def findRowCell (board, position):
    row = position//10
    cell = position%10 - 1
    return (row, cell)
    
def onBoard (position):
    rowCell = findRowCell (board, position)
    row = rowCell[0]
    cell = rowCell[1]
    if -1 < row < 8 and -1 < cell < 8 and -1 < position < 99:
        return True
    else:
        return False
    

def validMove (board, playerPiece, initialPosition, finalPosition): ##This Works
    global skippingPositions ## This helps in changing the global variable. Variables can't be accessed but only can be referenced without this statement
        
    ##Updates Valid Positions when the Opponent Piece is in the valid position (i.e skips)    

    initialValidPositions = initialValidPositionList(board, initialPosition)
    updatedValidPositions = updateValidPosition(board, initialPosition, initialValidPositions)
                

    if finalPosition in updatedValidPositions: #Checks if final Position is a valid position
        if type(findPiece(board, finalPosition)) == int: #Checks if the player piece or opponentPiece is not already in final position. If it is not, then return!
            return True
    return False
    

def isAtEnd (piece, position):  #Check if the piece is at the end
    rowCell = findRowCell (board, position)
    row = rowCell[0]
    if piece == "o" and row == 7:
        return True
    if piece == "x" and row == 0:
        return True
    return False
        

def changePiece (piece, position): #If at the end, change piece to capital to denote that it is king
    rowCell = findRowCell (board, position)
    row = rowCell[0]
    cell = rowCell[1]
    if piece == "o":
        board[row][cell] = "O"
    if piece == "x":
        board[row][cell] = "X"
    return board
    
def isWinner (board, player1, player2):
    player1Count = 0
    player2Count = 0
    if player1 == "x":
        player1King = "X"
        player2King = "O"
    if player2 == "x":
        player1King = "O"
        player2King = "X"
    for row in board:
        for cell in row:
            if cell == player1 or cell == player1King:
                player1Count = player1Count + 1
            if cell == player2 or cell == player2King:
                player2Count= player2Count + 1
    
    if player1Count == 0:
        print ("player2 won")
        return player2
        
    if player2Count == 0:
        print ("player1 won")
        return player1
        
    return False
            

def main ():
    moveCount = 0
    player1 = choosingPiece()
    player2 = otherPlayerPiece (player1)
    printBoard(startingBoard(board))
    while isWinner(board, player1, player2) == False:
        movePiece (board, moveCount, player1, player2)
        moveCount = moveCount + 1
        printBoard(board)

main()