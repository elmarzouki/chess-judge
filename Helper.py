"""
This Helper file contain methods and vars to help
the players to focus only on the best move to make
on the BoardGame
"""
from Properties import *


# check if the move within the board boundaries
def IsWithinTheBoundaries(Target):
    if Target[0] >= 0 and Target[0] < 8 and Target[1] >= 0 and Target[1] < 8: return True
    return False


# check if the new position ain't reserved by non of the same army
def IsNoConflict(GameBoard, CurrentPosition, TargetPosition):
    if GameBoard[TargetPosition[0]][TargetPosition[1]] is Empty: return True
    Colors = [WHITE, BLACK]
    for Color in Colors:
        if GameBoard[CurrentPosition[0]][CurrentPosition[1]].startswith(Color) and \
            GameBoard[TargetPosition[0]][TargetPosition[1]].startswith(Color): return False
    return True


# get the army on the board
def GetArmy(Color, GameBoard):
    Army = []
    for i in range(8):
        for j in range(8):
            if GameBoard[i][j] is not Empty:
                if GameBoard[i][j].startswith(Color):
                    Army.append({'Piece': GameBoard[i][j], 'Position': (i, j)})
    return Army

# get the color of the enemy
def GetEnemyColor(Color):
    if Color == WHITE: return BLACK
    return WHITE


def GetKingPsition(BotTurn,GameBoard):
    Army = GetArmy(BotTurn, GameBoard)
    for Soldier in Army:
        if Soldier['Piece'] == BotTurn+King:
            return Soldier['Position']
