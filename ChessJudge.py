"""
    about:
    This code was written by Mostafa El-Marzouki @iSuperMostafa
    and Fady Safwat
    ------------------------------------------------------------
    summery:
    this judge allows you to focus on choosing the best position to play
    chess game Just by write your code in BotNumOne or BotNumTwo
    ------------------------------------------------------------
    Note:
    This version does not include: en passant - castling
"""
import random
from Helper import *




class ChessJudge:
    def __init__(self, BotNumOneObj, BotNumTwoObj):

        self.GameBoard = [[Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                          [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                          [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                          [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                          [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                          [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                          [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
                          [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty]]




        self.BotNumOne = {'Name': Empty, 'Color': Empty, 'Play': BotNumOneObj}
        self.BotNumTwo = {'Name': Empty, 'Color': Empty, 'Play': BotNumTwoObj}

        self.BotTurn = BLACK

        self.IsGameEnded = False

        self.Winner = Empty


        self.__GoFirst__()




    # place the players pieces on the board
    def __PlaceThePieces__(self):
        for i in range(0, 8):
            self.GameBoard[1][i] = WHITE + Pawn
            self.GameBoard[6][i] = BLACK + Pawn
        self.GameBoard[0] = [WHITE + Rook, WHITE + Knight, WHITE + Bishop, WHITE + King, WHITE + Queen,
                             WHITE + Bishop, WHITE + Knight, WHITE + Rook]
        self.GameBoard[7] = [BLACK + Rook, BLACK + Knight, BLACK + Bishop, BLACK + King, BLACK + Queen,
                             BLACK + Bishop, BLACK + Knight, BLACK + Rook]




     # Randomly choose which bot to start the game
    def __GoFirst__(self):
        if random.choice((BLACK, WHITE)) == WHITE:
            self.BotNumOne['Color'] = WHITE
            self.BotNumTwo['Color'] = BLACK
        else:
            self.BotNumTwo['Color'] = WHITE
            self.BotNumOne['Color'] = BLACK
        self.__PlaceThePieces__()


# ------------------------------------------------------------------------------------------------------------------
# Promote  Pawn
# ----------------
    def PromotePawn(self,move):
        type,color = getPieceType(move,self.GameBoard)


        if self.BotNumOne['Color'] == color:
            if (move[0]== 0) and (color==BLACK) and (type==Pawn):
                new =  self.BotNumOne['Play'].PromoteAPawn(color)
                self.GameBoard[move[0]][move[1]] = new
        if self.BotNumTwo['Color'] == color:
            if (move[0]== 0) and (color==BLACK)and (type==Pawn):
                new =  self.BotNumTwo['Play'].PromoteAPawn(color)
                self.GameBoard[move[0]][move[1]] = new

        if self.BotNumOne['Color'] == color:
            if (move[0]== 7) and (color==WHITE)and (type==Pawn):
                new =  self.BotNumOne['Play'].PromoteAPawn(color)
                self.GameBoard[move[0]][move[1]] = new
        if self.BotNumTwo['Color'] == color:
            if (move[0]== 7) and (color==WHITE)and (type==Pawn):
                new =  self.BotNumTwo['Play'].PromoteAPawn(color)
                self.GameBoard[move[0]][move[1]] = new



# -------------------------------------------------------------------------------------------------------------------
# manage the game
# ---------------
    def TakeTurns(self):


        self.IsGameEnded =  self.IsGameEndedFun(self.GameBoard)

        #print ('-------------------------------------------------')
        #print('This is Bot 1 color: '+str(self.BotNumOne['Color']))
        #print('This is Bot 2 color: '+str(self.BotNumTwo['Color']))
        #print ('-------------------------------------------------')

        while not self.IsGameEnded:
            if self.BotTurn == self.BotNumOne['Color']:
                #print (0)
                #print (PiecePossibleMoves((7,0),self.GameBoard))
                piece,move = self.BotNumOne['Play'].Play(self.GameBoard,self.BotNumOne['Color'])

                if CheckMate(self.BotNumOne['Color'],self.GameBoard):
                    #print ('King in danger : ' +str(self.BotNumOne['Color'])+'********************************' )
                    while not MakeMoveCheckKingSafe(piece,move,self.GameBoard):
                        piece,move = self.BotNumOne['Play'].Play(self.GameBoard,self.BotNumOne['Color'])

                    #print (' this : '+str(piece) +' will go : '+str(move))
                    MakeMove(piece,move,self.GameBoard)
                    #print ('-------------------------------------------------------------------------------------------------')
                    #for row in self.GameBoard:print(row)
                    #print ('-------------------------------------------------------------------------------------------------')
                    self.PromotePawn(move)
                    self.IsGameEnded = self.IsGameEndedFun(self.GameBoard)
                    self.BotTurn = self.BotNumTwo['Color']
                else:
                    #print (' this : '+str(piece) +' will go : '+str(move))
                    MakeMove(piece,move,self.GameBoard)
                    #print ('-------------------------------------------------------------------------------------------------')
                    #for row in self.GameBoard:print(row)
                    #print ('-------------------------------------------------------------------------------------------------')
                    self.PromotePawn(move)
                    self.IsGameEnded = self.IsGameEndedFun(self.GameBoard)
                    self.BotTurn = self.BotNumTwo['Color']
            elif self.BotTurn == self.BotNumTwo['Color']:
                #print (1)
                piece,move = self.BotNumTwo['Play'].Play(self.GameBoard,self.BotNumTwo['Color'])

                if CheckMate(self.BotNumTwo['Color'],self.GameBoard):
                    #print ('King in danger : ' +str(self.BotNumTwo['Color']) +'********************************')
                    while not MakeMoveCheckKingSafe(piece,move,self.GameBoard):
                        piece,move = self.BotNumTwo['Play'].Play(self.GameBoard,self.BotNumTwo['Color'])

                    #print (' this : '+str(piece) +' will go : '+str(move))
                    MakeMove(piece,move,self.GameBoard)
                    #print ('-------------------------------------------------------------------------------------------------')
                    #for row in self.GameBoard:print(row)
                    #print ('-------------------------------------------------------------------------------------------------')
                    self.PromotePawn(move)
                    self.IsGameEnded = self.IsGameEndedFun(self.GameBoard)
                    self.BotTurn = self.BotNumOne['Color']
                else:
                    #print (' this : '+str(piece) +' will go : '+str(move))
                    MakeMove(piece,move,self.GameBoard)
                    #print ('-------------------------------------------------------------------------------------------------')
                    #for row in self.GameBoard:print(row)
                    #print ('-------------------------------------------------------------------------------------------------')
                    self.PromotePawn(move)
                    self.IsGameEnded = self.IsGameEndedFun(self.GameBoard)
                    self.BotTurn = self.BotNumOne['Color']
            #print ('BLACK: '+ str(GetArmy(BLACK, self.GameBoard)))
            #print ('WHITE: '+ str(GetArmy(WHITE, self.GameBoard)))
        #print ('xxxxxxxxxxxx')
        #for row in self.GameBoard:print(row)
        return self.Winner, self.GameBoard






# ----------------------------------------------------------------------------------------------------------------------
# Return true if game ended
    def IsGameEndedFun(self,gameBoard):

        b1 = False
        b2 = False
        w1 = False
        w2 = False
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
                            b1 = True
                            #return False
            if not kingPossibleMoves:
                 if self.BotNumOne['Color'] == BLACK:
                     self.Winner = self.BotNumTwo['Name']
                     if not b1:
                         return True
                 else:
                     self.Winner = self.BotNumOne['Name']
                     if not b1:
                         return True
        else:
            kingPosition = KingPsition(BLACK,gameBoard)
            kingPossibleMoves = PiecePossibleMoves(kingPosition,gameBoard)
            army = GetArmy(BLACK, gameBoard)
            army.remove(kingPosition)
            if (not army) and (not kingPossibleMoves):
                self.Winner = 'Draw'
                return True
            elif len(GetArmy(BLACK, gameBoard)) == len(GetArmy(WHITE, gameBoard)) == 1:
                self.Winner='Draw'
                return True
            else:
                army = GetArmy(BLACK, gameBoard)
                for piece in army:
                    if PiecePossibleMoves(piece,gameBoard):
                        b2 = True
                        #return False
                self.Winner='Draw'
                if not b2:
                    return True
    # for white king
        if CheckMate(WHITE,gameBoard):
            kingPosition = KingPsition(WHITE,gameBoard)
            kingPossibleMoves = PiecePossibleMoves(kingPosition,gameBoard)
            army = GetArmy(WHITE, gameBoard)
            for piece in army:
                piecePossibleMoves = PiecePossibleMoves(piece,gameBoard)
                if piecePossibleMoves:
                    for move in piecePossibleMoves:
                        if MakeMoveCheckKingSafe(piece,move,gameBoard):
                            w1 = True
                            #return False
            if not kingPossibleMoves:
                if self.BotNumOne['Color'] == WHITE:
                     self.Winner = self.BotNumTwo['Name']
                     if not w1:
                        return True
                else:
                     self.Winner = self.BotNumOne['Name']
                     if not w1:
                        return True
        else:
            kingPosition = KingPsition(WHITE,gameBoard)
            kingPossibleMoves = PiecePossibleMoves(kingPosition,gameBoard)
            army = GetArmy(WHITE, gameBoard)
            army.remove(kingPosition)
            if (not army) and (not kingPossibleMoves):
                self.Winner='Draw'
                return True
            elif len(GetArmy(BLACK, gameBoard)) == len(GetArmy(WHITE, gameBoard))== 1:
                self.Winner='Draw'
                return True
            else:
                army = GetArmy(WHITE, gameBoard)
                for piece in army:
                    if PiecePossibleMoves(piece,gameBoard):
                        #return False
                        w2 = True
                self.Winner='Draw'
                if not w2:
                    return True
        return False



    # set BotOne Name
    def SetBotOneName(self, Name):
        self.BotNumOne['Name'] = Name

    # set BotTwo Name
    def SetBotTwoName(self, Name):
        self.BotNumTwo['Name'] = Name
