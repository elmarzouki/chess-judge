"""
This Helper file contain methods and vars to help
the players to focus only on the best move to make
on the BoardGame
"""
WHITE = "White"
BLACK = "Black"
Pawn = "Pawn" # done
Rook = "Rook" # done
Knight = "Knight" # done
Bishop = "Bishop" # done
King = "King"
Queen = "Queen" # done
Empty = "None"
#TRUE = "TRUE"
#FALSE = "FALSE"


# ----------------------------------------------------------------------------------------------------------------------
# Return possible moves for any piece
# position = (Number,Number)
def PiecePossibleMoves(position,gameBoard):

    possibleMoves = []

    if (IsWithinTheBoundaries(position)) and not (gameBoard[position[0]][position[1]] == Empty): pass
    else: return possibleMoves

    row = position[0]
    column = position[1]
    type,color = getPieceType(position,gameBoard)

    enemyArmy = GetArmy(GetEnemyColor(color), gameBoard)
    enemyPossibleMoves = EnemyPossibleMoves(enemyArmy,gameBoard)

# ------------------------------------------------------------------------------------------------------------------
# for white pawn moves
    if type == Pawn:
        if (row == 1) and (color == WHITE):
            if gameBoard[row+1][column] == Empty:
                if MakeMoveCheckKingSafe(position,(row+1, column),gameBoard):
                    possibleMoves.append((row+1, column))
            if (gameBoard[row+2][column] == Empty) and (gameBoard[row+1][column] == Empty):
                if MakeMoveCheckKingSafe(position,(row+2, column),gameBoard):
                    possibleMoves.append((row+2, column))
            if (IsWithinTheBoundaries((row+1, column+1))) and not (gameBoard[row+1][column+1].startswith(color)) and not (gameBoard[row+1][column+1]== Empty):
                if MakeMoveCheckKingSafe(position,(row+1, column+1),gameBoard):
                    possibleMoves.append((row+1, column+1))
            if (IsWithinTheBoundaries((row+1, column-1))) and not (gameBoard[row+1][column-1].startswith(color)) and not (gameBoard[row+1][column-1]== Empty):
                if MakeMoveCheckKingSafe(position,(row+1, column-1),gameBoard):
                    possibleMoves.append((row+1, column-1))
        else:
            if (IsWithinTheBoundaries((row+1, column))) and (color == WHITE) and (gameBoard[row+1][column] == Empty):
                if MakeMoveCheckKingSafe(position,(row+1, column),gameBoard):
                    possibleMoves.append((row+1, column))
            if (IsWithinTheBoundaries((row+1, column+1))) and (color == WHITE) and not (gameBoard[row+1][column+1].startswith(color)) and not (gameBoard[row+1][column+1]== Empty):
                if MakeMoveCheckKingSafe(position,(row+1, column+1),gameBoard):
                    possibleMoves.append((row+1, column+1))
            if (IsWithinTheBoundaries((row+1, column-1))) and (color == WHITE) and not (gameBoard[row+1][column-1].startswith(color)) and not (gameBoard[row+1][column-1]== Empty):
                if MakeMoveCheckKingSafe(position,(row+1, column-1),gameBoard):
                    possibleMoves.append((row+1, column-1))
    # --------------------------------------------------------------------------------------------------------------
    # for black pawn moves
        if (row == 6) and (color == BLACK):
            if gameBoard[row-1][column] == Empty:
                if MakeMoveCheckKingSafe(position,(row-1, column),gameBoard):
                    possibleMoves.append((row-1, column))
            if (gameBoard[row-2][column] == Empty) and (gameBoard[row-1][column] == Empty):
                if MakeMoveCheckKingSafe(position,(row-2, column),gameBoard):
                    possibleMoves.append((row-2, column))
            if (IsWithinTheBoundaries((row-1, column+1))) and not (gameBoard[row-1][column+1].startswith(color)) and not (gameBoard[row-1][column+1]== Empty):
                if MakeMoveCheckKingSafe(position,(row-1, column+1),gameBoard):
                    possibleMoves.append((row-1, column+1))
            if (IsWithinTheBoundaries((row-1, column-1))) and not (gameBoard[row-1][column-1].startswith(color)) and not (gameBoard[row-1][column-1]== Empty):
                if MakeMoveCheckKingSafe(position,(row-1, column-1),gameBoard):
                    possibleMoves.append((row-1, column-1))
        else:
            if (IsWithinTheBoundaries((row-1, column))) and (color == BLACK) and (gameBoard[row-1][column] == Empty):
                if MakeMoveCheckKingSafe(position,(row-1, column),gameBoard):
                    possibleMoves.append((row-1, column))
            if (IsWithinTheBoundaries((row-1, column+1))) and (color == BLACK) and not(gameBoard[row-1][column+1].startswith(color)) and not (gameBoard[row-1][column+1]== Empty):
                if MakeMoveCheckKingSafe(position,(row-1, column+1),gameBoard):
                    possibleMoves.append((row-1, column+1))
            if (IsWithinTheBoundaries((row-1, column-1))) and (color == BLACK) and not (gameBoard[row-1][column-1].startswith(color)) and not (gameBoard[row-1][column-1]== Empty):
                if MakeMoveCheckKingSafe(position,(row-1, column-1),gameBoard):
                    possibleMoves.append((row-1, column-1))
    # --------------------------------------------------------------------------------------------------------------
    # for rook moves
    elif type == Rook:
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow-1, column))) and (gameBoard[xrow-1][column] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow-1, column),gameBoard):
                    possibleMoves.append((xrow-1, column))
                    xrow = xrow-1
            elif (IsWithinTheBoundaries((xrow-1, column))) and not (gameBoard[xrow-1][column].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow-1, column),gameBoard):
                    possibleMoves.append((xrow-1, column))
                    break
            else: break
        xrow = row
        for i in range(8):
            if (IsWithinTheBoundaries((xrow+1, column))) and (gameBoard[xrow+1][column] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow+1, column),gameBoard):
                    possibleMoves.append((xrow+1, column))
                    xrow = xrow+1
            elif (IsWithinTheBoundaries((xrow+1, column))) and not (gameBoard[xrow+1][column].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow+1, column),gameBoard):
                    possibleMoves.append((xrow+1, column))
                    break
            else: break
        xrow = row
        for i in range(8):
            if (IsWithinTheBoundaries((row, xcolumn+1))) and (gameBoard[row][xcolumn+1] == Empty):
                if MakeMoveCheckKingSafe(position,(row, xcolumn+1),gameBoard):
                    possibleMoves.append((row, xcolumn+1))
                    xcolumn = xcolumn+1
            elif (IsWithinTheBoundaries((row, xcolumn+1))) and not (gameBoard[row][xcolumn+1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(row, xcolumn+1),gameBoard):
                    possibleMoves.append((row, xcolumn+1))
                    break
            else: break
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((row, xcolumn-1))) and (gameBoard[row][xcolumn-1] == Empty):
                if MakeMoveCheckKingSafe(position,(row, xcolumn-1),gameBoard):
                    possibleMoves.append((row, xcolumn-1))
                    xcolumn = xcolumn-1
            elif (IsWithinTheBoundaries((row, xcolumn-1))) and not (gameBoard[row][xcolumn-1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(row, xcolumn-1),gameBoard):
                    possibleMoves.append((row, xcolumn-1))
                    break
            else: break
        xcolumn = column
    # --------------------------------------------------------------------------------------------------------------
    # for knight moves
    if type == Knight:
        if (IsWithinTheBoundaries((row-2, column+1))) and not(gameBoard[row-2][column+1].startswith(color)):
            if MakeMoveCheckKingSafe(position,(row-2, column+1),gameBoard):
                possibleMoves.append((row-2, column+1))
        if (IsWithinTheBoundaries((row-2, column-1))) and not(gameBoard[row-2][column-1].startswith(color)):
            if MakeMoveCheckKingSafe(position,(row-2, column-1),gameBoard):
                possibleMoves.append((row-2, column-1))
        if (IsWithinTheBoundaries((row-1, column+2))) and not(gameBoard[row-1][column+2].startswith(color)):
            if MakeMoveCheckKingSafe(position,(row-1, column+2),gameBoard):
                possibleMoves.append((row-1, column+2))
        if (IsWithinTheBoundaries((row-1, column-2))) and not(gameBoard[row-1][column-2].startswith(color)):
            if MakeMoveCheckKingSafe(position,(row-1, column-2),gameBoard):
                possibleMoves.append((row-1, column-2))
        if (IsWithinTheBoundaries((row+1, column+2))) and not(gameBoard[row+1][column+2].startswith(color)):
            if MakeMoveCheckKingSafe(position,(row+1, column+2),gameBoard):
                possibleMoves.append((row+1, column+2))
        if (IsWithinTheBoundaries((row+1, column-2))) and not(gameBoard[row+1][column-2].startswith(color)):
            if MakeMoveCheckKingSafe(position,(row+1, column-2),gameBoard):
                possibleMoves.append((row+1, column-2))
        if (IsWithinTheBoundaries((row+2, column+1))) and not(gameBoard[row+2][column+1].startswith(color)):
            if MakeMoveCheckKingSafe(position,(row+2, column+1),gameBoard):
                possibleMoves.append((row+2, column+1))
        if (IsWithinTheBoundaries((row+2, column-1))) and not(gameBoard[row+2][column-1].startswith(color)):
            if MakeMoveCheckKingSafe(position,(row+2, column-1),gameBoard):
                possibleMoves.append((row+2, column-1))
    # --------------------------------------------------------------------------------------------------------------
    # for bishop moves
    if type == Bishop:
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow-1, xcolumn+1))) and (gameBoard[xrow-1][xcolumn+1] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow-1, xcolumn+1),gameBoard):
                    possibleMoves.append((xrow-1, xcolumn+1))
                xrow = xrow-1
                xcolumn = xcolumn+1
            elif (IsWithinTheBoundaries((xrow-1, xcolumn+1))) and not (gameBoard[xrow-1][xcolumn+1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow-1, xcolumn+1),gameBoard):
                    possibleMoves.append((xrow-1, xcolumn+1))
                break
            else: break
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow-1, xcolumn-1))) and (gameBoard[xrow-1][xcolumn-1] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow-1, xcolumn-1),gameBoard):
                    possibleMoves.append((xrow-1, xcolumn-1))
                xrow = xrow-1
                xcolumn = xcolumn-1
            elif (IsWithinTheBoundaries((xrow-1, xcolumn-1))) and not (gameBoard[xrow-1][xcolumn-1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow-1, xcolumn-1),gameBoard):
                    possibleMoves.append((xrow-1, xcolumn-1))
                break
            else: break
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow+1, xcolumn+1))) and (gameBoard[xrow+1][xcolumn+1] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow+1, xcolumn+1),gameBoard):
                    possibleMoves.append((xrow+1, xcolumn+1))
                xrow = xrow+1
                xcolumn = xcolumn+1

            elif (IsWithinTheBoundaries((xrow+1, xcolumn+1))) and not (gameBoard[xrow+1][xcolumn+1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow+1, xcolumn+1),gameBoard):
                    possibleMoves.append((xrow+1, xcolumn+1))
                break
            else: break
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow+1, xcolumn-1))) and (gameBoard[xrow+1][xcolumn-1] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow+1, xcolumn-1),gameBoard):
                    possibleMoves.append((xrow+1, xcolumn-1))
                xrow = xrow+1
                xcolumn = xcolumn-1
            elif (IsWithinTheBoundaries((xrow+1, xcolumn-1))) and not (gameBoard[xrow+1][xcolumn-1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow+1, xcolumn-1),gameBoard):
                    possibleMoves.append((xrow+1, xcolumn-1))
                break
            else: break
        xrow = row
        xcolumn = column
    # --------------------------------------------------------------------------------------------------------------
    # for queen moves
    if type == Queen:
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow-1, xcolumn+1))) and (gameBoard[xrow-1][xcolumn+1] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow-1, xcolumn+1),gameBoard):
                    possibleMoves.append((xrow-1, xcolumn+1))
                xrow = xrow-1
                xcolumn = xcolumn+1
            elif (IsWithinTheBoundaries((xrow-1, xcolumn+1))) and not (gameBoard[xrow-1][xcolumn+1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow-1, xcolumn+1),gameBoard):
                    possibleMoves.append((xrow-1, xcolumn+1))
                break
            else: break
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow-1, xcolumn-1))) and (gameBoard[xrow-1][xcolumn-1] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow-1, xcolumn-1),gameBoard):
                    possibleMoves.append((xrow-1, xcolumn-1))
                xrow = xrow-1
                xcolumn = xcolumn-1
            elif (IsWithinTheBoundaries((xrow-1, xcolumn-1))) and not (gameBoard[xrow-1][xcolumn-1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow-1, xcolumn-1),gameBoard):
                    possibleMoves.append((xrow-1, xcolumn-1))
                break
            else: break
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow+1, xcolumn+1))) and (gameBoard[xrow+1][xcolumn+1] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow+1, xcolumn+1),gameBoard):
                    possibleMoves.append((xrow+1, xcolumn+1))
                xrow = xrow+1
                xcolumn = xcolumn+1
            elif (IsWithinTheBoundaries((xrow+1, xcolumn+1))) and not (gameBoard[xrow+1][xcolumn+1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow+1, xcolumn+1),gameBoard):
                    possibleMoves.append((xrow+1, xcolumn+1))
                break
            else: break
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow+1, xcolumn-1))) and (gameBoard[xrow+1][xcolumn-1] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow+1, xcolumn-1),gameBoard):
                    possibleMoves.append((xrow+1, xcolumn-1))
                xrow = xrow+1
                xcolumn = xcolumn-1
            elif (IsWithinTheBoundaries((xrow+1, xcolumn-1))) and not (gameBoard[xrow+1][xcolumn-1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow+1, xcolumn-1),gameBoard):
                    possibleMoves.append((xrow+1, xcolumn-1))
                break
            else: break
        xrow = row
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((xrow-1, column))) and (gameBoard[xrow-1][column] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow-1, column),gameBoard):
                    possibleMoves.append((xrow-1, column))
                xrow = xrow-1
            elif (IsWithinTheBoundaries((xrow-1, column))) and not (gameBoard[xrow-1][column].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow-1, column),gameBoard):
                    possibleMoves.append((xrow-1, column))
                break
            else: break
        xrow = row
        for i in range(8):
            if (IsWithinTheBoundaries((xrow+1, column))) and (gameBoard[xrow+1][column] == Empty):
                if MakeMoveCheckKingSafe(position,(xrow+1, column),gameBoard):
                    possibleMoves.append((xrow+1, column))
                xrow = xrow+1
            elif (IsWithinTheBoundaries((xrow+1, column))) and not (gameBoard[xrow+1][column].startswith(color)):
                if MakeMoveCheckKingSafe(position,(xrow+1, column),gameBoard):
                    possibleMoves.append((xrow+1, column))
                break
            else: break
        xrow = row
        for i in range(8):
            if (IsWithinTheBoundaries((row, xcolumn+1))) and (gameBoard[row][xcolumn+1] == Empty):
                if MakeMoveCheckKingSafe(position,(row, xcolumn+1),gameBoard):
                    possibleMoves.append((row, xcolumn+1))
                xcolumn = xcolumn+1
            elif (IsWithinTheBoundaries((row, xcolumn+1))) and not (gameBoard[row][xcolumn+1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(row, xcolumn+1),gameBoard):
                    possibleMoves.append((row, xcolumn+1))
                break
            else: break
        xcolumn = column
        for i in range(8):
            if (IsWithinTheBoundaries((row, xcolumn-1))) and (gameBoard[row][xcolumn-1] == Empty):
                if MakeMoveCheckKingSafe(position,(row, xcolumn-1),gameBoard):
                    possibleMoves.append((row, xcolumn-1))
                xcolumn = xcolumn-1
            elif (IsWithinTheBoundaries((row, xcolumn-1))) and not (gameBoard[row][xcolumn-1].startswith(color)):
                if MakeMoveCheckKingSafe(position,(row, xcolumn-1),gameBoard):
                    possibleMoves.append((row, xcolumn-1))
                break
            else: break
        xcolumn = column
    # --------------------------------------------------------------------------------------------------------------
    # for king moves
    if type == King:
        if (IsWithinTheBoundaries((row-1, column-1))) and not(gameBoard[row-1][column-1].startswith(color)) and not ((row-1, column-1) in enemyPossibleMoves):
             if MakeMoveCheckKingSafe(position,(row-1, column-1),gameBoard):
                 possibleMoves.append((row-1, column-1))
        if (IsWithinTheBoundaries((row-1, column))) and not(gameBoard[row-1][column].startswith(color))and not((row-1, column) in enemyPossibleMoves):
             if MakeMoveCheckKingSafe(position,(row-1, column),gameBoard):
                 possibleMoves.append((row-1, column))
        if (IsWithinTheBoundaries((row-1, column+1))) and not(gameBoard[row-1][column+1].startswith(color))and not((row-1, column+1) in enemyPossibleMoves):
             if MakeMoveCheckKingSafe(position,(row-1, column+1),gameBoard):
                 possibleMoves.append((row-1, column+1))
        if (IsWithinTheBoundaries((row, column-1))) and not(gameBoard[row][column-1].startswith(color))and not((row, column-1) in enemyPossibleMoves):
             if MakeMoveCheckKingSafe(position,(row, column-1),gameBoard):
                possibleMoves.append((row, column-1))
        if (IsWithinTheBoundaries((row, column+1))) and not(gameBoard[row][column+1].startswith(color))and not((row, column+1) in enemyPossibleMoves):
             if MakeMoveCheckKingSafe(position,(row, column+1),gameBoard):
                 possibleMoves.append((row, column+1))
        if (IsWithinTheBoundaries((row+1, column-1))) and not(gameBoard[row+1][column-1].startswith(color))and not ((row+1, column-1) in enemyPossibleMoves):
             if MakeMoveCheckKingSafe(position,(row+1, column-1),gameBoard):
                 possibleMoves.append((row+1, column-1))
        if (IsWithinTheBoundaries((row+1, column))) and not(gameBoard[row+1][column].startswith(color))and not((row+1, column) in enemyPossibleMoves):
             if MakeMoveCheckKingSafe(position,(row+1, column),gameBoard):
                 possibleMoves.append((row+1, column))
        if (IsWithinTheBoundaries((row+1, column+1))) and not(gameBoard[row+1][column+1].startswith(color))and not((row+1, column+1) in enemyPossibleMoves):
             if MakeMoveCheckKingSafe(position,(row+1, column+1),gameBoard):
                 possibleMoves.append((row+1, column+1))
    # --------------------------------------------------------------------------------------------------------------
    #print('this is possible moves in PiecePossibleMoves: ' + str(possibleMoves))
    return possibleMoves
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Return enemy possible moves
def EnemyPossibleMoves(enemyArmy,gameBoard):

    enemyPossibleMoves = []

    for position in enemyArmy:
        row = position[0]
        column = position[1]
        type,color = getPieceType(position,gameBoard)
        # ----------------------------------------------------------------------------------------------------------
        # for white pawn moves
        if type == Pawn:
            #if (row == 1) and (color == WHITE):
            #    if gameBoard[row+1][column] == Empty:
            #        enemyPossibleMoves.append((row+1, column))
            #    if gameBoard[row+2][column] == Empty:
            #        enemyPossibleMoves.append((row+2, column))
            if (IsWithinTheBoundaries((row+1, column+1))) and not (gameBoard[row+1][column+1].startswith(color)) and (color == WHITE):
                enemyPossibleMoves.append((row+1, column+1))
            if (IsWithinTheBoundaries((row+1, column-1))) and not (gameBoard[row+1][column-1].startswith(color)) and (color == WHITE):
                enemyPossibleMoves.append((row+1, column-1))

            if (IsWithinTheBoundaries((row-1, column+1))) and not (gameBoard[row-1][column+1].startswith(color)) and (color == BLACK):
                enemyPossibleMoves.append((row-1, column+1))
            if (IsWithinTheBoundaries((row-1, column-1))) and not (gameBoard[row-1][column-1].startswith(color)) and (color == BLACK):
                enemyPossibleMoves.append((row-1, column-1))

           # else:
                #if (IsWithinTheBoundaries((row+1, column))) and (gameBoard[row][column] == WHITE) and (gameBoard[row+1][column] == Empty):
                    #enemyPossibleMoves.append((row+1, column))
               # if (IsWithinTheBoundaries((row+1, column+1))) and (gameBoard[row][column] == WHITE) and (gameBoard[row+1][column+1] == BLACK):
                #    enemyPossibleMoves.append((row+1, column+1))
                #if (IsWithinTheBoundaries((row+1, column-1))) and (gameBoard[row][column] == WHITE) and (gameBoard[row+1][column-1] == BLACK):
                 #   enemyPossibleMoves.append((row+1, column-1))
        # ----------------------------------------------------------------------------------------------------------
        # for black pawn moves
        #    if (row == 6) and (color == BLACK):
        #        if gameBoard[row-1][column] == Empty:
        #            enemyPossibleMoves.append((row-1, column))
        #        if gameBoard[row-2][column] == Empty:
        #            enemyPossibleMoves.append((row-2, column))
        #        if (IsWithinTheBoundaries((row-1, column+1))) and (gameBoard[row-1][column+1] == WHITE):
        #            enemyPossibleMoves.append((row-1, column+1))
        #        if (IsWithinTheBoundaries((row-1, column-1))) and (gameBoard[row-1][column-1] == WHITE):
        #            enemyPossibleMoves.append((row-1, column-1))
        #    else:
        #        if (IsWithinTheBoundaries((row-1, column))) and (gameBoard[row][column] == BLACK) and (gameBoard[row-1][column] == Empty):
        #            enemyPossibleMoves.append((row-1, column))
        #        if (IsWithinTheBoundaries((row-1, column+1))) and (gameBoard[row][column] == BLACK) and (gameBoard[row-1][column+1] == WHITE):
        #            enemyPossibleMoves.append((row-1, column+1))
        #        if (IsWithinTheBoundaries((row-1, column-1))) and (gameBoard[row][column] == BLACK) and (gameBoard[row-1][column-1] == WHITE):
        #            enemyPossibleMoves.append((row-1, column-1))
        # ----------------------------------------------------------------------------------------------------------
        # for rook moves
        elif type == Rook:
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow-1, column))) and (gameBoard[xrow-1][column] == Empty):
                    enemyPossibleMoves.append((xrow-1, column))
                    xrow = xrow-1
                elif (IsWithinTheBoundaries((xrow-1, column))) and not (gameBoard[xrow-1][column].startswith(color)):
                    enemyPossibleMoves.append((xrow-1, column))
                    break
                else: break
            xrow = row
            for i in range(8):
                if (IsWithinTheBoundaries((xrow+1, column))) and (gameBoard[xrow+1][column] == Empty):
                    enemyPossibleMoves.append((xrow+1, column))
                    xrow = xrow+1
                elif (IsWithinTheBoundaries((xrow+1, column))) and not (gameBoard[xrow+1][column].startswith(color)):
                    enemyPossibleMoves.append((xrow+1, column))
                    break
                else: break
            xrow = row
            for i in range(8):
                if (IsWithinTheBoundaries((row, xcolumn+1))) and (gameBoard[row][xcolumn+1] == Empty):
                    enemyPossibleMoves.append((row, xcolumn+1))
                    xcolumn = xcolumn+1
                elif (IsWithinTheBoundaries((row, xcolumn+1))) and not (gameBoard[row][xcolumn+1].startswith(color)):
                    enemyPossibleMoves.append((row, xcolumn+1))
                    break
                else: break
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((row, xcolumn-1))) and (gameBoard[row][xcolumn-1] == Empty):
                    enemyPossibleMoves.append((row, xcolumn-1))
                    xcolumn = xcolumn-1
                elif (IsWithinTheBoundaries((row, xcolumn-1))) and not (gameBoard[row][xcolumn-1].startswith(color)):
                    enemyPossibleMoves.append((row, xcolumn-1))
                    break
                else: break
            xcolumn = column
    # --------------------------------------------------------------------------------------------------------------
    # for knight moves
        if type == Knight:
            if (IsWithinTheBoundaries((row-2, column+1))) and not(gameBoard[row-2][column+1].startswith(color)):
                enemyPossibleMoves.append((row-2, column+1))
            if (IsWithinTheBoundaries((row-2, column-1))) and not(gameBoard[row-2][column-1].startswith(color)):
                enemyPossibleMoves.append((row-2, column-1))
            if (IsWithinTheBoundaries((row-1, column+2))) and not(gameBoard[row-1][column+2].startswith(color)):
                enemyPossibleMoves.append((row-1, column+2))
            if (IsWithinTheBoundaries((row-1, column-2))) and not(gameBoard[row-1][column-2].startswith(color)):
                enemyPossibleMoves.append((row-1, column-2))
            if (IsWithinTheBoundaries((row+1, column+2))) and not(gameBoard[row+1][column+2].startswith(color)):
                enemyPossibleMoves.append((row+1, column+2))
            if (IsWithinTheBoundaries((row+1, column-2))) and not(gameBoard[row+1][column-2].startswith(color)):
                enemyPossibleMoves.append((row+1, column-2))
            if (IsWithinTheBoundaries((row+2, column+1))) and not(gameBoard[row+2][column+1].startswith(color)):
                enemyPossibleMoves.append((row+2, column+1))
            if (IsWithinTheBoundaries((row+2, column-1))) and not(gameBoard[row+2][column-1].startswith(color)):
                enemyPossibleMoves.append((row+2, column-1))
    # --------------------------------------------------------------------------------------------------------------
    # for bishop moves
        if type == Bishop:
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow-1, xcolumn+1))) and (gameBoard[xrow-1][xcolumn+1] == Empty):
                    enemyPossibleMoves.append((xrow-1, xcolumn+1))
                    xrow = xrow-1
                    xcolumn = xcolumn+1
                elif (IsWithinTheBoundaries((xrow-1, xcolumn+1))) and not (gameBoard[xrow-1][xcolumn+1].startswith(color)):
                    enemyPossibleMoves.append((xrow-1, xcolumn+1))
                    break
                else: break
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow-1, xcolumn-1))) and (gameBoard[xrow-1][xcolumn-1] == Empty):
                    enemyPossibleMoves.append((xrow-1, xcolumn-1))
                    xrow = xrow-1
                    xcolumn = xcolumn-1
                elif (IsWithinTheBoundaries((xrow-1, xcolumn-1))) and not (gameBoard[xrow-1][xcolumn-1].startswith(color)):
                    enemyPossibleMoves.append((xrow-1, xcolumn-1))
                    break
                else: break
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow+1, xcolumn+1))) and (gameBoard[xrow+1][xcolumn+1] == Empty):
                    enemyPossibleMoves.append((xrow+1, xcolumn+1))
                    xrow = xrow+1
                    xcolumn = xcolumn+1
                elif (IsWithinTheBoundaries((xrow+1, xcolumn+1))) and not (gameBoard[xrow+1][xcolumn+1].startswith(color)):
                    enemyPossibleMoves.append((xrow+1, xcolumn+1))
                    break
                else: break
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow+1, xcolumn-1))) and (gameBoard[xrow+1][xcolumn-1] == Empty):
                    enemyPossibleMoves.append((xrow+1, xcolumn-1))
                    xrow = xrow+1
                    xcolumn = xcolumn-1
                elif (IsWithinTheBoundaries((xrow+1, xcolumn-1))) and not (gameBoard[xrow+1][xcolumn-1].startswith(color)):
                    enemyPossibleMoves.append((xrow+1, xcolumn-1))
                    break
                else: break
            xrow = row
            xcolumn = column
    # --------------------------------------------------------------------------------------------------------------
    # for queen moves
        if type == Queen:
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow-1, xcolumn+1))) and (gameBoard[xrow-1][xcolumn+1] == Empty):
                    enemyPossibleMoves.append((xrow-1, xcolumn+1))
                    xrow = xrow-1
                    xcolumn = xcolumn+1
                elif (IsWithinTheBoundaries((xrow-1, xcolumn+1))) and not (gameBoard[xrow-1][xcolumn+1].startswith(color)):
                    enemyPossibleMoves.append((xrow-1, xcolumn+1))
                    break
                else: break
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow-1, xcolumn-1))) and (gameBoard[xrow-1][xcolumn-1] == Empty):
                    enemyPossibleMoves.append((xrow-1, xcolumn-1))
                    xrow = xrow-1
                    xcolumn = xcolumn-1
                elif (IsWithinTheBoundaries((xrow-1, xcolumn-1))) and not (gameBoard[xrow-1][xcolumn-1].startswith(color)):
                    enemyPossibleMoves.append((xrow-1, xcolumn-1))
                    break
                else: break
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow+1, xcolumn+1))) and (gameBoard[xrow+1][xcolumn+1] == Empty):
                    enemyPossibleMoves.append((xrow+1, xcolumn+1))
                    xrow = xrow+1
                    xcolumn = xcolumn+1
                elif (IsWithinTheBoundaries((xrow+1, xcolumn+1))) and not (gameBoard[xrow+1][xcolumn+1].startswith(color)):
                    enemyPossibleMoves.append((xrow+1, xcolumn+1))
                    break
                else: break
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow+1, xcolumn-1))) and (gameBoard[xrow+1][xcolumn-1] == Empty):
                    enemyPossibleMoves.append((xrow+1, xcolumn-1))
                    xrow = xrow+1
                    xcolumn = xcolumn-1
                elif (IsWithinTheBoundaries((xrow+1, xcolumn-1))) and not (gameBoard[xrow+1][xcolumn-1].startswith(color)):
                    enemyPossibleMoves.append((xrow+1, xcolumn-1))
                    break
                else: break
            xrow = row
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((xrow-1, column))) and (gameBoard[xrow-1][column] == Empty):
                    enemyPossibleMoves.append((xrow-1, column))
                    xrow = xrow-1
                elif (IsWithinTheBoundaries((xrow-1, column))) and not (gameBoard[xrow-1][column].startswith(color)):
                    enemyPossibleMoves.append((xrow-1, column))
                    break
                else: break
            xrow = row
            for i in range(8):
                if (IsWithinTheBoundaries((xrow+1, column))) and (gameBoard[xrow+1][column] == Empty):
                    enemyPossibleMoves.append((xrow+1, column))
                    xrow = xrow+1
                elif (IsWithinTheBoundaries((xrow+1, column))) and not (gameBoard[xrow+1][column].startswith(color)):
                    enemyPossibleMoves.append((xrow+1, column))
                    break
                else: break
            xrow = row
            for i in range(8):
                if (IsWithinTheBoundaries((row, xcolumn+1))) and (gameBoard[row][xcolumn+1] == Empty):
                    enemyPossibleMoves.append((row, xcolumn+1))
                    xcolumn = xcolumn+1
                elif (IsWithinTheBoundaries((row, xcolumn+1))) and not (gameBoard[row][xcolumn+1].startswith(color)):
                    enemyPossibleMoves.append((row, xcolumn+1))
                    break
                else: break
            xcolumn = column
            for i in range(8):
                if (IsWithinTheBoundaries((row, xcolumn-1))) and (gameBoard[row][xcolumn-1] == Empty):
                    enemyPossibleMoves.append((row, xcolumn-1))
                    xcolumn = xcolumn-1
                elif (IsWithinTheBoundaries((row, xcolumn-1))) and not (gameBoard[row][xcolumn-1].startswith(color)):
                    enemyPossibleMoves.append((row, xcolumn-1))
                    break
                else: break
            xcolumn = column
    # --------------------------------------------------------------------------------------------------------------
    # for king moves
        if type == King:
            if (IsWithinTheBoundaries((row-1, column-1))) and not(gameBoard[row-1][column-1].startswith(color)):
                enemyPossibleMoves.append((row-1, column-1))
            if (IsWithinTheBoundaries((row-1, column))) and not(gameBoard[row-1][column].startswith(color)):
                enemyPossibleMoves.append((row-1, column))
            if (IsWithinTheBoundaries((row-1, column+1))) and not(gameBoard[row-1][column+1].startswith(color)):
                enemyPossibleMoves.append((row-1, column+1))
            if (IsWithinTheBoundaries((row, column-1))) and not(gameBoard[row][column-1].startswith(color)):
                enemyPossibleMoves.append((row, column-1))
            if (IsWithinTheBoundaries((row, column+1))) and not(gameBoard[row][column+1].startswith(color)):
                enemyPossibleMoves.append((row, column+1))
            if (IsWithinTheBoundaries((row+1, column-1))) and not(gameBoard[row+1][column-1].startswith(color)):
                enemyPossibleMoves.append((row+1, column-1))
            if (IsWithinTheBoundaries((row+1, column))) and not(gameBoard[row+1][column].startswith(color)):
                enemyPossibleMoves.append((row+1, column))
            if (IsWithinTheBoundaries((row+1, column+1))) and not(gameBoard[row+1][column+1].startswith(color)):
                enemyPossibleMoves.append((row+1, column+1))
    # --------------------------------------------------------------------------------------------------------------
    #print('this is possible moves in EnemyPossibleMoves: ' + str(enemyPossibleMoves))
    return enemyPossibleMoves
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Return true if we moved this piece and the king will stay safe
def MakeMoveCheckKingSafe(Current,Target,gameBoard):
    from copy import copy, deepcopy
    gameboard = deepcopy(gameBoard)
    gameboard[Target[0]][Target[1]] = gameboard[Current[0]][Current[1]]
    gameboard[Current[0]][Current[1]] = Empty
    type,color = getPieceType(Current,gameBoard)
    enemyArmy = GetArmy(GetEnemyColor(color), gameboard)
    enemyPossibleMoves = EnemyPossibleMoves(enemyArmy,gameboard)
    kingPosition = KingPsition(color,gameboard)
    if kingPosition in enemyPossibleMoves:
        return False
    else: return True
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Retuen true if king is checked
def CheckMate(Color,gameBoard):

    enemyArmy = GetArmy(GetEnemyColor(Color), gameBoard)
    enemyPossibleMoves = EnemyPossibleMoves(enemyArmy,gameBoard)
    kingPosition = KingPsition(Color,gameBoard)


    if kingPosition in enemyPossibleMoves:
        return True
    else: return False
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Return true if game ended
'''
def IsGameEnded(gameBoard):
    # for black king
    if CheckMate(BLACK,gameBoard):
        kingPosition = KingPsition(BLACK,gameBoard)
        kingPossibleMoves = PiecePossibleMoves(kingPosition,gameBoard)
        army = GetArmy(BLACK, gameBoard)
        for piece in army:
            piecePossibleMoves = PiecePossibleMoves(piece,gameBoard)
            if piecePossibleMoves:
                for move in piecePossibleMoves:
                    if MakeMoveCheckKingSafe(piece,move,gameBoard):
                        return False
        if not kingPossibleMoves:
            return True
    else:
        kingPosition = KingPsition(BLACK,gameBoard)
        kingPossibleMoves = PiecePossibleMoves(kingPosition,gameBoard)
        army = GetArmy(BLACK, gameBoard)
        army.remove(kingPosition)
        if (not army) and (not kingPossibleMoves):
            return True
        elif len(GetArmy(BLACK, gameBoard)) == len(GetArmy(WHITE, gameBoard)) ==  1:
            return True
        else:
            for piece in army:
                if PiecePossibleMoves(piece,gameBoard):
                    return False
            return True
    # for white king
    if CheckMate(WHITE,gameBoard):
        kingPosition = KingPsition(WHITE,gameBoard)
        kingPossibleMoves = PiecePossibleMoves(kingPosition,gameBoard)
        army = GetArmy(WHITE, GameBoard)
        for piece in army:
            piecePossibleMoves = PiecePossibleMoves(piece,gameBoard)
            if piecePossibleMoves:
                for move in piecePossibleMoves:
                    if MakeMoveCheckKingSafe(piece,move,gameBoard):
                        return False
        if not kingPossibleMoves:
            return True
    else:
        kingPosition = KingPsition(WHITE,gameBoard)
        kingPossibleMoves = PiecePossibleMoves(kingPosition,gameBoard)
        army = GetArmy(WHITE, GameBoard)
        army.remove(kingPosition)
        if (not army) and (not kingPossibleMoves):
            return True
        elif len(GetArmy(BLACK, gameBoard)) == len(GetArmy(WHITE, gameBoard))== 1:
            return True
        else:
            for piece in army:
                if PiecePossibleMoves(piece,gameBoard):
                    return False
            return True
'''
# ----------------------------------------------------------------------------------------------------------------------
# Return army
def GetArmy(Color, GameBoard):
    Army = []
    for i in range(8):
        for j in range(8):
            if GameBoard[i][j] is not Empty:
                if GameBoard[i][j].startswith(Color):
                    Army.append((i, j))
    return Army
# ----------------------------------------------------------------------------------------------------------------------
# Return enemy color
def GetEnemyColor(Color):
    if Color == WHITE: return BLACK
    return WHITE
# ----------------------------------------------------------------------------------------------------------------------
# Return true if position in the board
def IsWithinTheBoundaries(Target):
    #if not Target:print (Target)
    if (Target[0] >= 0) and (Target[0] < 8) and (Target[1] >= 0) and (Target[1] < 8): return True
    return False
# ----------------------------------------------------------------------------------------------------------------------
# Return piece type and color
def getPieceType(position,gameBoard):
    fullpiece = gameBoard[position[0]][position[1]]
    color = Empty
    piece = Empty
    if fullpiece.startswith(WHITE):
        piece = fullpiece.replace(WHITE, "")
        color = WHITE
    elif fullpiece.startswith(BLACK):
        piece = fullpiece.replace(BLACK, "")
        color = BLACK
    return piece,color
# ----------------------------------------------------------------------------------------------------------------------
# Return king position
def KingPsition(Color,GameBoard):
    army = GetArmy(Color, GameBoard)
    for piece in army:
        if GameBoard[piece[0]][piece[1]].endswith(King):
            return piece
# ----------------------------------------------------------------------------------------------------------------------
# make move
def MakeMove(piece,move,gameBoard):
    gameBoard[move[0]][move[1]] = gameBoard[piece[0]][piece[1]]
    gameBoard[piece[0]][piece[1]] = Empty
