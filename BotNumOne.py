

"""
summery:
this judge allows you to focus on choosing the best position to play
Chess game Just by write your code in BotNumOne or BotNumTwo
------------------------------------------------------------
this dummy bot chooses positions randomly
you can edit it and check the game board assigned in 'GameBoard', 
and your Color will be B|W assigned randomly in 'Color':
your code must contain "Play" function that return position
that's the position you want to make your move in
and a PromoteAPawn function that return the piece that will 
replace your promoted pawn and it sould be like 'Color + self.Rook'

NOTE: Empty = None

function in helper :


---------
PiecePossibleMoves(position,gameBoard): 
position like (rowNumber,columnNumber)
return list of possible moves for a piece whic in the position u sent
---------
EnemyPossibleMoves(enemyArmy,gameBoard):
enemyArmy is a list or all enemy positions
return list of possible moves for all enemy pieces
---------
MakeMoveCheckKingSafe(Current,Target,gameBoard):
Current like (rowNumber,columnNumber)
Target like (rowNumber,columnNumber)
return true if king will be safe else false
---------
CheckMate(Color,gameBoard):
return true if king is checked else false
---------
IsGameEnded(gameBoard):
return true if game ended else false
----------
GetArmy(Color, GameBoard):
return list of my army positins
------------
GetEnemyColor(Color):
Return enemy color
------------
IsWithinTheBoundaries(Target):
target like (rowNumber,columnNumber)
Return true if position in the board
------------
getPieceType(position,gameBoard):
position like (rowNumber,columnNumber)
return type,color
-----------
KingPsition(Color,GameBoard):
Return king position
-----------


"""









import random

class ChessBot:
    def __init__(self, Helper):
        self.Helper = Helper
        self.GameBoard = self.Helper.Empty
        self.Color = self.Helper.Empty
        self.Opponent = self.Helper.Empty
        self.Empty = self.Helper.Empty
        self.WHITE = self.Helper.WHITE
        self.BLACK = self.Helper.BLACK
        self.Pawn = self.Helper.Pawn
        self.Rook = self.Helper.Rook
        self.Knight = self.Helper.Knight
        self.Bishop = self.Helper.Bishop
        self.King = self.Helper.King
        self.Queen = self.Helper.Queen


    def Play(self, GameBoard, Color):
        army = self.Helper.GetArmy(Color, GameBoard)
        piece = random.choice(army)
        AvailableMoves = self.Helper.PiecePossibleMoves(piece,GameBoard)
        if AvailableMoves:
            move = random.choice(AvailableMoves)
        else:

            while not AvailableMoves:
                piece = random.choice(army)
                AvailableMoves = self.Helper.PiecePossibleMoves(piece,GameBoard)
                if AvailableMoves:
                    move = random.choice(AvailableMoves)

        return piece,move


    def PromoteAPawn(self, Color):
        return Color + self.Queen
