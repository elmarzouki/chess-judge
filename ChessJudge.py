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
from copy import copy, deepcopy

"""
increment the stack depth allowed
with this, deeper recursive calls will be possible
"""
import sys
sys.setrecursionlimit(2000000000)


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
        self.BotTurn = WHITE
        self.IsGameEnded = False
        self.IsGameStarted = False
        self.Winner = Empty
        self.BlackKingFreeMoves = []
        self.WhiteKingFreeMoves = []
        self.WhiteCheck = False
        self.BlackCheck = False
        self.DangerWhite =[]
        self.DangerBlack =[]
        self.SpareBoard = deepcopy(self.GameBoard)


    def __PlaceThePieces__(self):
        """
        place the players pieces on the board
        :return:
        """
        for i in range(0, 8):
            self.GameBoard[1][i] = WHITE + Pawn
            self.GameBoard[6][i] = BLACK + Pawn
        self.GameBoard[0] = [WHITE + Rook, WHITE + Knight, WHITE + Bishop, WHITE + King, WHITE + Queen,
                             WHITE + Bishop, WHITE + Knight, WHITE + Rook]
        self.GameBoard[7] = [BLACK + Rook, BLACK + Knight, BLACK + Bishop, BLACK + King, BLACK + Queen,
                             BLACK + Bishop, BLACK + Knight, BLACK + Rook]
        self.SpareBoard = deepcopy(self.GameBoard)

        self.IsGameStarted = True


    def __GoFirst__(self):
        """
        Randomly choose which bot to start the game
        :return:
        """
        if random.choice((BLACK, WHITE)) == WHITE:
            self.BotNumOne['Color'] = WHITE
            self.BotNumTwo['Color'] = BLACK
        else:
            self.BotNumTwo['Color'] = WHITE
            self.BotNumOne['Color'] = BLACK
        self.__PlaceThePieces__()


    def __IsValidRookMove__(self, Current, Target):
        """
        check if Rook move is valid
        :param Current: tuple of the rook current position
        :param Target: tuple of the rook target position
        :return: if the rook move is valid or not
        """
        Color = self.GameBoard[Current[0]][Current[1]].replace(Rook, "")
        Start, End = 0, 0
        if Current == Target: return FALSE
        if Current[0] == Target[0]:
            if Target[1] > Current[1]:
                Start = Current[1]
                End = Target[1]
            elif Target[1] < Current[1]:
                Start = Target[1]
                End = Current[1]
            for i in range(Start, End):
                if self.GameBoard[Current[0]][i]==Target:
                    if self.GameBoard[Current[0]][i] is not Empty and (self.GameBoard[Current[0]][i].startswith(Color)):return FALSE
                elif self.GameBoard[Current[0]][i] is not Empty: return FALSE
            return TRUE
        elif Current[1] == Target[1]:
            if Target[0] > Current[0]:
                Start = Current[0]
                End = Target[0]
            elif Target[0] < Current[0]:
                Start = Target[0]
                End = Current[0]
            for i in range(Start, End):
                if self.GameBoard[Current[0]][i]==Target:
                    if self.GameBoard[Current[0]][i] is not Empty and (self.GameBoard[Current[0]][i].startswith(Color)):return FALSE
                elif self.GameBoard[Current[0]][i] is not Empty: return FALSE
            return TRUE
        return FALSE


    def __IsValidBishopMove__(self, Current, Target):
        """
        check if Bishop move is valid
        :param Current: tuple of the Bishop current position
        :param Target: tuple of the Bishop target position
        :return: if the Bishop move is valid or not
        """
        if Current==Target:return FALSE
        """ coming from the NW to SE """
        if Target[0] > Current[0] and Target[1] > Current[1]:
            if Target[0] - Current[0] is Target[1] - Current[1]:
                End = Target[1] - Current[1]
                for iterator in range(1, End):
                    if self.GameBoard[Current[0] + iterator][Current[1] + iterator] is not Empty: return FALSE
                return TRUE
            """ coming from NE to SW """
        elif Target[0] > Current[0] and Target[1] < Current[1]:
            if Target[0] - Current[0] is Current[1] - Target[1]:
                End = Current[1] - Target[1]
                for iterator in range(1, End):
                    if self.GameBoard[Current[0] + iterator][Current[1] - iterator] is not Empty: return FALSE
                return TRUE
            """ coming from SW to NE """
        elif Target[0] < Current[0] and Target[1] > Current[1]:
            if Current[0] - Target[0] is Target[1] - Current[1]:
                End = Target[1] - Current[1]
                for iterator in range(1, End):
                    if self.GameBoard[Current[0] - iterator][Current[1] + iterator] is not Empty: return FALSE
                return TRUE
            """ coming from SE to NW """
        elif Target[0] < Current[0] and Target[1] < Current[1]:
            if Current[0] - Target[0] is Current[1] - Target[1]:
                End = Current[1] - Target[1]
                for iterator in range(1, End):
                    if self.GameBoard[Current[0] - iterator][Current[1] - iterator] is not Empty: return FALSE
                return TRUE
        return FALSE


    def __IsValidMove__(self, Current, Target):
        """
        check if the move is valid
        :param Current: tuple of the piece current position
        :param Target: tuple of the piece target position
        :return: if the piece move is valid or not
        """
        if IsWithinTheBoundaries(Target) and not self.GameBoard[Target[0]][Target[1]].endswith(King):
            """ Black Pawn """
            if self.GameBoard[Current[0]][Current[1]] == BLACK + Pawn:
                if Target[1] == Current[1] and self.GameBoard[Target[0]][Target[1]] is Empty:
                    if Current[0] == 6 and Target[0] == 4 and self.GameBoard[5][Target[1]] is Empty: return TRUE  # the pawn two steps forward case
                    if Target[0] == Current[0] - 1:
                        if Target[0] == 0: return MOVE_PROMOTE
                        return TRUE
                if (Target[1] == Current[1] + 1) or (Target[1] == Current[1] - 1):
                    if Target[0] == Current[0] - 1:
                        if self.GameBoard[Target[0]][Target[1]].startswith(WHITE):
                            if Target[0] == 0: return MOVE_PROMOTE
                return FALSE
            """ White Pawn """
            if self.GameBoard[Current[0]][Current[1]] == WHITE + Pawn:
                if Target[1] == Current[1] and self.GameBoard[Target[0]][Target[1]] is Empty:
                    if Current[0] == 1 and Target[0] == 3 and self.GameBoard[2][Target[1]] is Empty: return TRUE  # the pawn two steps forward case
                    if Target[0] == Current[0] + 1:
                        if Target[0] == 7: return MOVE_PROMOTE
                        return TRUE
                if (Target[1] == Current[1] + 1) or (Target[1] == Current[1] - 1):
                    if Target[0] == Current[0] + 1:
                        if self.GameBoard[Target[0]][Target[1]].startswith(BLACK):
                            if Target[0] == 7: return MOVE_PROMOTE
                return FALSE
            """ Rook """
            if self.GameBoard[Current[0]][Current[1]].endswith(Rook):
                return self.__IsValidRookMove__(Current, Target)
            """ Knight """
            if self.GameBoard[Current[0]][Current[1]].endswith(Knight):
                KnightMoves = [(Current[0]+1, Current[1]+2),(Current[0]+1, Current[1]-2),
                               (Current[0]-1, Current[1]+2), (Current[0]-1, Current[1]-2),
                               (Current[0]+2, Current[1]+1),(Current[0]+2, Current[1]-1),
                               (Current[0]-2, Current[1]+1),(Current[0]-2, Current[1]-1)]
                for Move in KnightMoves:
                    if Target[0] == Move[0] and Target[1] == Move[1]: return TRUE
                return FALSE
                # if ((Target[0] is Current[0]+1) or (Target[0] is Current[0]-1)) \
                #         and ((Target[1] is Current[1]+2) or (Target[1] is Current[1]-2)):
                #     return True
                # elif ((Target[0] is Current[0]+2) or (Target[0] is Current[0]-2)) \
                #         and ((Target[1] is Current[1]+1) or (Target[1] is Current[1]-1)):
                #     return True
            """ Bishop """
            if self.GameBoard[Current[0]][Current[1]].endswith(Bishop):
                return self.__IsValidBishopMove__(Current, Target)
            """ Queen """
            if self.GameBoard[Current[0]][Current[1]].endswith(Queen):
                if self.__IsValidBishopMove__(Current, Target) is TRUE: return TRUE
                return self.__IsValidRookMove__(Current, Target)
            """ King """
            if self.GameBoard[Current[0]][Current[1]].endswith(King):
                KingMoves = [(Current[0]+1, Current[1]), (Current[0]-1, Current[1]), (Current[0], Current[1]+1),
                             (Current[0], Current[1]-1), (Current[0]+1, Current[1]-1), (Current[0]-1, Current[1]+1),
                             (Current[0]+1, Current[1]+1), (Current[0]-1, Current[1]-1)]
                for Move in KingMoves:
                    if Target[0] == Move[0] and Target[1] == Move[1]:
                        Color = self.GameBoard[Current[0]][Current[1]].replace(King, "")
                        Enemy = GetArmy(GetEnemyColor(Color), self.GameBoard)
                        for Soldier in Enemy:
                            if self.__IsValidMove__(Soldier['Position'], Target)is TRUE: return FALSE
                        return TRUE
        return FALSE


    def __MakeMove__(self, Current, Target):
        """
        place the player's move on the board
        :param Current: tuple of the piece current position
        :param Target: tuple of the piece target position
        :return:
        """
        if (IsNoConflict(self.GameBoard, Current, Target)):
            if self.__IsValidMove__(Current, Target) is MOVE_PROMOTE:
                self.__CheckMate__(Current, Target)
                print('******************************************Promote************************************************************************************')
                print(Current,Target)
                if (self.BotTurn == BLACK):
                    if not self.BlackCheck:
                        if not self.__CheckMate__(Current, Target):
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__GetPromoted__(Target)
                                self.__PrintTheMove__(Current,Target)
                        else:
                            self.__PickAnotherMove__()
                    else:
                        if (Target in self.DangerBlack):
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__GetPromoted__(Target)
                                self.__PrintTheMove__(Current,Target)
                        else:
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__GetPromoted__(Target)
                                self.__PrintTheMove__(Current,Target)
                elif (self.BotTurn == WHITE):
                    if not self.WhiteCheck:
                        if not self.__CheckMate__(Current, Target):
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__GetPromoted__(Target)
                                self.__PrintTheMove__(Current,Target)
                        else:
                            self.__PickAnotherMove__()
                    else:
                        if (Target in self.DangerWhite):
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__GetPromoted__(Target)
                                self.__PrintTheMove__(Current,Target)
                        else:
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__GetPromoted__(Target)
                                self.__PrintTheMove__(Current,Target)
            elif self.__IsValidMove__(Current, Target)is TRUE:
                print('----------------------------------------------------------------------------------------------------------')
                self.__CheckMate__(Current, Target)
                # Check For CheckMate For BlackKing---------------------------------------------------------------------
                if (self.BotTurn == BLACK):
                    if not self.BlackCheck:
                        # No CheckMate situation------------------------------------------------------------------------
                        # TO make Sure King will not be checked if moved to a target------------------------------------
                        if not self.__CheckMate__(Current, Target):
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__PrintTheMove__(Current,Target)
                        else:
                            self.__PickAnotherMove__()
                        # ----------------------------------------------------------------------------------------------
                    # CheckMate Situation-------------------------------------------------------------------------------
                    else:
                        print('CheckMat '+str(self.BlackCheck)+' Black')
                        #print(self.DangerBlack)
                        #print(Current,Target)
                        # ForBOtOne-------------------------------------------------------------------------------------

                        KingPosition = GetKingPsition(self.BotTurn, self.GameBoard)
                        if (Current==KingPosition):
                            if not self.__CheckMate__(Current, Target):
                                self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                                self.GameBoard[Current[0]][Current[1]] = Empty
                                if self.__AmIChecked__():
                                    self.__PickAnotherMove__()
                                else:
                                    self.__PrintTheMove__(Current,Target)
                        elif (Target in self.DangerBlack):
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__PrintTheMove__(Current,Target)
                        else:
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__PrintTheMove__(Current,Target)
                        # ----------------------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------
                # Check for CheckMate for WhiteKing---------------------------------------------------------------------
                elif (self.BotTurn == WHITE):
                    if not self.WhiteCheck:
                        if not self.__CheckMate__(Current, Target):
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__PrintTheMove__(Current,Target)
                        else:
                            self.__PickAnotherMove__()
                    else:
                        print('CheckMat '+str(self.WhiteCheck)+' White')
                        #print(self.DangerWhite)
                        #print(Current,Target)
                        KingPosition = GetKingPsition(self.BotTurn, self.GameBoard)
                        if (Current==KingPosition):
                            if not self.__CheckMate__(Current, Target):
                                self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                                self.GameBoard[Current[0]][Current[1]] = Empty
                                if self.__AmIChecked__():
                                    self.__PickAnotherMove__()
                                else:
                                    self.__PrintTheMove__(Current,Target)
                            else:
                                self.__PickAnotherMove__()
                        elif (Target in self.DangerWhite):
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__PrintTheMove__(Current,Target)
                        else:
                            self.GameBoard[Target[0]][Target[1]] = self.GameBoard[Current[0]][Current[1]]
                            self.GameBoard[Current[0]][Current[1]] = Empty
                            if self.__AmIChecked__():
                                self.__PickAnotherMove__()
                            else:
                                self.__PrintTheMove__(Current,Target)
            else:
                self.__PickAnotherMove__()
        else:
            self.__PickAnotherMove__()

    def __PickAnotherMove__(self):
        self.GameBoard = deepcopy(self.SpareBoard)
        if self.BotNumOne['Color'] == self.BotTurn:
            Current, Target = self.BotNumOne['Play'].play(self.GameBoard, self.BotNumOne['Color'])
            self.__MakeMove__(Current, Target)
        elif self.BotNumTwo['Color'] == self.BotTurn:
            Current, Target = self.BotNumTwo['Play'].play(self.GameBoard, self.BotNumTwo['Color'])
            self.__MakeMove__(Current, Target)

    def __PrintTheMove__(self,Current,Target):
         self.SpareBoard = deepcopy(self.GameBoard)
         if self.BotNumOne['Color'] == self.BotTurn:
             print(self.BotNumOne['Color'] ,self.BotNumOne['Name'], "Played", Current, "In", Target)
         elif self.BotNumTwo['Color'] == self.BotTurn:
             print(self.BotNumTwo['Color'] ,self.BotNumTwo['Name'], "Played", Current, "In", Target)

    def __AmIChecked__(self):
        if self.BotNumOne['Color'] == self.BotTurn:
            KingPosition = GetKingPsition(self.BotTurn,self.GameBoard)
            Enemy = GetArmy(GetEnemyColor(self.BotTurn), self.GameBoard)
            for Soldier in Enemy:
                if self.__IsValidKing__(Soldier['Position'], KingPosition)is TRUE:
                    return True
            return False
        elif self.BotNumTwo['Color'] == self.BotTurn:
            KingPosition = GetKingPsition(self.BotTurn,self.GameBoard)
            Enemy = GetArmy(GetEnemyColor(self.BotTurn), self.GameBoard)
            for Soldier in Enemy:
                if self.__IsValidKing__(Soldier['Position'], KingPosition)is TRUE:
                    return True
            return False

    def __IsValidKing__(self, Current, Target):
        if IsWithinTheBoundaries(Target):
            """ Black Pawn """
            if self.GameBoard[Current[0]][Current[1]] == BLACK + Pawn:
                #if Target[1] == Current[1] and self.GameBoard[Target[0]][Target[1]] is Empty:
                #    if Current[0] == 6 and Target[0] == 4 and self.GameBoard[5][Target[1]] is Empty: return True  # the pawn two steps forward case
                #    if Target[0] == Current[0] - 1:
                #        if Target[0] == 0: return MOVE_PROMOTE
                #        return True
                if (Target[1] == Current[1] + 1) or (Target[1] == Current[1] - 1):
                    if Target[0] == Current[0] - 1:
                        if self.GameBoard[Target[0]][Target[1]].startswith(WHITE) or (self.GameBoard[Target[0]][Target[1]]is Empty): return TRUE
                return FALSE
            """ White Pawn """
            if self.GameBoard[Current[0]][Current[1]] == WHITE + Pawn:
                #if Target[1] == Current[1] and self.GameBoard[Target[0]][Target[1]] is Empty:
                #    if Current[0] == 1 and Target[0] == 3 and self.GameBoard[2][Target[1]] is Empty: return True  # the pawn two steps forward case
                #    if Target[0] == Current[0] + 1:
                #        if Target[0] == 7: return MOVE_PROMOTE
                #        return True
                if (Target[1] == Current[1] + 1) or (Target[1] == Current[1] - 1):
                    if Target[0] == Current[0] + 1:
                        if (self.GameBoard[Target[0]][Target[1]].startswith(BLACK)) or (self.GameBoard[Target[0]][Target[1]]is Empty): return TRUE
                return FALSE
            """ Rook """
            if self.GameBoard[Current[0]][Current[1]].endswith(Rook):
                return self.__IsValidRookMove__(Current, Target)
            """ Knight """
            if self.GameBoard[Current[0]][Current[1]].endswith(Knight):
                KnightMoves = [(Current[0]+1, Current[1]+2),(Current[0]+1, Current[1]-2),
                               (Current[0]-1, Current[1]+2), (Current[0]-1, Current[1]-2),
                               (Current[0]+2, Current[1]+1),(Current[0]+2, Current[1]-1),
                               (Current[0]-2, Current[1]+1),(Current[0]-2, Current[1]-1)]
                for Move in KnightMoves:
                    if Target[0] == Move[0] and Target[1] == Move[1]: return TRUE
                return FALSE

            """ Bishop """
            if self.GameBoard[Current[0]][Current[1]].endswith(Bishop):
                return self.__IsValidBishopMove__(Current, Target)
            """ Queen """
            if self.GameBoard[Current[0]][Current[1]].endswith(Queen):
                if (self.__IsValidBishopMove__(Current, Target)is TRUE) or (self.__IsValidRookMove__(Current, Target)is TRUE): return TRUE
                else:return FALSE
            """ King """
            if self.GameBoard[Current[0]][Current[1]].endswith(King):
                KingMoves = [(Current[0]+1, Current[1]), (Current[0]-1, Current[1]), (Current[0], Current[1]+1),
                             (Current[0], Current[1]-1), (Current[0]+1, Current[1]-1), (Current[0]-1, Current[1]+1),
                             (Current[0]+1, Current[1]+1), (Current[0]-1, Current[1]-1)]
                for Move in KingMoves:
                    if Target[0] == Move[0] and Target[1] == Move[1]:
                        Color = self.GameBoard[Current[0]][Current[1]].replace(King, "")
                        Enemy = GetArmy(GetEnemyColor(Color), self.GameBoard)
                        for Soldier in Enemy:
                            if self.__IsValidKing__(Soldier['Position'], Target)is TRUE: return FALSE
                        return TRUE
        return FALSE

    def __CheckMate__(self,Current, Target):
        self.BlackCheck = False
        self.WhiteCheck = False
        self.DangerBlack = []
        self.DangerWhite = []
        if self.BotNumOne['Color'] == self.BotTurn:
            KingPosition = GetKingPsition(self.BotTurn, self.GameBoard)
            #print(str(KingPosition)+' Kinggggggggggggggggggggggggggggg'+str(self.BotTurn))
            self.__IsKingAlive__(self.BotTurn+King)
            Enemy = GetArmy(GetEnemyColor(self.BotTurn), self.GameBoard)
            for Soldier in Enemy:
                if self.__IsValidKing__(Soldier['Position'], KingPosition)is TRUE:
                    print('Checkkkkkkkkkkkkkk********************************************************************************************Mateeeeeeeeeeeee')
                    print('Solder Position-'+str(Soldier['Position'])+'King Position-'+str(KingPosition))
                    if (self.BotTurn == BLACK):
                        self.BlackCheck = True
                        self.DangerBlack.append(Soldier['Position'])
                    elif (self.BotTurn == WHITE):
                        self.DangerWhite.append(Soldier['Position'])
                        self.WhiteCheck = True
            if (self.BotTurn == BLACK):
                #print('Current'+str(Current))
                if (Current==KingPosition):
                    if Target in self.BlackKingFreeMoves:
                        #print('Yes')
                        return False
                    else:
                        #print(str(Target)+"Not A Validddddddddddddddddddd Moveeeeeeeeeeee -*King Will die*---------------------------")
                        return True
            elif (self.BotTurn == WHITE):
                #print('Current'+str(Current))
                if (Current==KingPosition):
                    if Target in self.WhiteKingFreeMoves:
                        #print('Yes')
                        return False
                    else:
                        #print(str(Target)+"Not A Validddddddddddddddddddd Moveeeeeeeeeeee -*King Will die*---------------------------")
                        return True


            #print('PlayNoCheckMate-----------------------------------------------------------*****---------------------------'+str(self.WhiteCheck)+'--------'+str(self.BlackCheck))
            return False

        elif self.BotNumTwo['Color'] == self.BotTurn:
            KingPosition = GetKingPsition(self.BotTurn, self.GameBoard)
            #print(str(KingPosition)+' Kinggggggggggggggggggggggggggggg'+str(self.BotTurn))
            self.__IsKingAlive__(self.BotTurn+King)
            Enemy = GetArmy(GetEnemyColor(self.BotTurn), self.GameBoard)
            for Soldier in Enemy:
                if self.__IsValidKing__(Soldier['Position'], KingPosition)is TRUE:
                    print('Checkkkkkkkkkkkkkk********************************************************************************************Mateeeeeeeeeeeee')
                    print('Solder Position-'+str(Soldier['Position'])+'King Position-'+str(KingPosition))
                    if (self.BotTurn == BLACK):
                        self.BlackCheck = True
                        self.DangerBlack.append(Soldier['Position'])
                    elif (self.BotTurn == WHITE):
                        self.WhiteCheck = True
                        self.DangerWhite.append(Soldier['Position'])
            if (self.BotTurn == BLACK):
                #print('Current'+str(Current))
                if (Current==KingPosition):
                    if Target in self.BlackKingFreeMoves:
                        #print('Yes')
                        return False
                    else:
                        #print(str(Target)+"Not A Validddddddddddddddddddd Moveeeeeeeeeeee -*King Will die*-------------------------")
                        return True
            elif (self.BotTurn == WHITE):
                #print('Current'+str(Current))
                if (Current==KingPosition):
                    if Target in self.WhiteKingFreeMoves:
                        #print('Yes')
                        return False
                    else:
                        #print(str(Target)+"Not A Validddddddddddddddddddd Moveeeeeeeeeeee -*King Will die*--------------------------")
                        return True


            #print('PlayNoCheckMate----------------------------------------------------*****----------------------------------'+str(self.WhiteCheck)+'--------'+str(self.BlackCheck))
            return False

    # get piece's position
    def __GetPiecePosition(self, Piece):
        for i in range(8):
            for j in range(8):
                if self.GameBoard[i][j] == Piece: return (i,j)

    def __Why__(self, Current, KingMoves, KING):
        print("Because")
        print(KING, "at", Current)
        for Move in KingMoves:
            if IsWithinTheBoundaries(Move):
                print(self.GameBoard[Move[0]][Move[1]], "at", Move)

    # check if king still alive
    def __IsKingAlive__(self, KING):
        FreeArea = []
        Danger =[]
        self.WhiteKingFreeMoves=[]
        self.BlackKingFreeMoves=[]
        Current = self.__GetPiecePosition(KING)
        KingMoves = [(Current[0] + 1, Current[1]), (Current[0] - 1, Current[1]), (Current[0], Current[1] + 1),
                     (Current[0], Current[1] - 1), (Current[0] + 1, Current[1] - 1), (Current[0] - 1, Current[1] + 1),
                     (Current[0] + 1, Current[1] + 1), (Current[0] - 1, Current[1] - 1)]



        if (KING == WHITE + King):
            Enemy = GetArmy(BLACK, self.GameBoard)
            #print(Enemy)
            #print(KingMoves)
            for Move in KingMoves:
                if self.__IsValidMove__(Current, Move)is TRUE:
                    FreeArea.append(Move)
                    if (self.GameBoard[Move[0]][Move[1]] is Empty)or (self.GameBoard[Move[0]][Move[1]].startswith(BLACK)):
                        if IsWithinTheBoundaries(Move):
                            #print(KingMoves)
                            #print(self.GameBoard[Move[0]][Move[1]])
                            for Soldier in Enemy:
                                #print(str(Soldier['Piece'])+str(Soldier['Position'])+'Targeeeet'+str(Move))
                                if self.__IsValidKing__(Soldier['Position'],Move)is TRUE:
                                    #print(self.__IsValidKing__(Soldier['Position'],Move))
                                    if Move in Danger:
                                        pass
                                    else:
                                        Danger.append(Move)
                                        #print('------------------------------------------------------------------------------------------------'+str(Soldier['Position'])+'WillKill'+str(Move))

            for Position in FreeArea:
                if IsWithinTheBoundaries(Position):
                    if Position not in Danger:
                        if (self.GameBoard[Position[0]][Position[1]] is Empty) or (self.GameBoard[Position[0]][Position[1]].startswith(BLACK)):
                            self.WhiteKingFreeMoves.append(Position)
            #print("WhiteKingFreeMoves=", self.WhiteKingFreeMoves)
            #print(FreeArea)
            MyArmy = GetArmy(WHITE,self.GameBoard)
            if not (FreeArea) and ((self.WhiteCheck) or (len(MyArmy)==1)):
                for piece in MyArmy:
                    if self.__IsValidKing__(piece['Position'],self.DangerBlack)is TRUE:
                        print(str(piece['Position'])+'Can Kill'+str(self.DangerBlack))
                        return  True
                print("Why?")
                self.__Why__(Current, KingMoves, KING)
                return False
            #if not FreeArea:
            #    print("Why?")
            #    self.__Why__(Current, KingMoves, KING)
            #    return False


        elif (KING == BLACK + King):
            Enemy = GetArmy(WHITE, self.GameBoard)
            #print(KingMoves)
            #print(Enemy)
            for Move in KingMoves:
                if self.__IsValidMove__(Current, Move)is TRUE:
                    FreeArea.append(Move)

                    if (self.GameBoard[Move[0]][Move[1]] is Empty)or (self.GameBoard[Move[0]][Move[1]].startswith(WHITE)):
                        if IsWithinTheBoundaries(Move):
                            #print(KingMoves)
                            #print(self.GameBoard[Move[0]][Move[1]])
                            for Soldier in Enemy:
                                #print(str(Soldier['Piece'])+str(Soldier['Position'])+'Targeeeet'+str(Move))
                                if self.__IsValidKing__(Soldier['Position'],Move)is TRUE:
                                    #print(self.__IsValidKing__(Soldier['Position'],Move))
                                    if Move in Danger:
                                        pass
                                    else:
                                        Danger.append(Move)
                                        #print('------------------------------------------------------------------------------------------------'+str(Soldier['Position'])+'WillKill'+str(Move))
            #print(FreeArea)
            for Position in FreeArea:
                if IsWithinTheBoundaries(Position):
                    if Position not in Danger:
                        if (self.GameBoard[Position[0]][Position[1]] is Empty) or (self.GameBoard[Position[0]][Position[1]].startswith(WHITE)):
                            self.BlackKingFreeMoves.append(Position)

            #print("BlackKingFreeMoves=", self.BlackKingFreeMoves)
            #print(FreeArea)
            MyArmy = GetArmy(BLACK,self.GameBoard)
            if not (FreeArea) and ((self.BlackCheck) or (len(MyArmy)==1)):
                for piece in MyArmy:
                    if self.__IsValidKing__(piece['Position'],self.DangerWhite)is TRUE:
                        print(str(piece['Position'])+'Can Kill'+str(self.DangerBlack))
                        return  True
                print("Why?")
                self.__Why__(Current, KingMoves, KING)
                return False
            #if not FreeArea:
            #    print("Why?")
            #    self.__Why__(Current, KingMoves, KING)
            #    return False

        return True

    # who is the winner
    def __IsWinner__(self):
        Colors = [BLACK, WHITE]
        for Color in Colors:
            Alive = self.__IsKingAlive__(Color+King)
            if not Alive:
                self.IsGameEnded = True
                if Color == self.BotNumOne['Color']:
                    return self.BotNumTwo['Name']
                elif Color == self.BotNumTwo['Color']:
                    return self.BotNumOne['Name']

    # place the player's moves while the game not ended
    def TakeTurns(self):
        # self.__Display__()
        if not self.IsGameStarted:
            self.__GoFirst__()
        while not self.IsGameEnded:
            if self.BotNumOne['Color'] == self.BotTurn:
                Current, Target = self.BotNumOne['Play'].play(self.GameBoard, self.BotNumOne['Color'])
                self.__MakeMove__(Current, Target)
                #print(self.BotNumOne['Name'], "Played", Current, "In", Target)
                self.Winner = self.__IsWinner__()
                self.BotTurn = self.BotNumTwo['Color']
                for row in self.GameBoard:print(row)

            elif self.BotNumTwo['Color'] == self.BotTurn:
                Current, Target = self.BotNumTwo['Play'].play(self.GameBoard, self.BotNumTwo['Color'])
                self.__MakeMove__(Current, Target)
                #print(self.BotNumTwo['Name'], "Played", Current, "In", Target)
                self.Winner = self.__IsWinner__()
                self.BotTurn = self.BotNumOne['Color']
                for row in self.GameBoard:print(row)

        return self.Winner, self.GameBoard

    # get promotion for pawn
    def __GetPromoted__(self, Position):
        Piece = self.GameBoard[Position[0]][Position[1]]
        if Piece.endswith(Pawn):
            Color = Piece.replace(Pawn, "")
            if Color == self.BotNumOne['Color']:
                self.GameBoard[Position[0]][Position[1]] = self.BotNumOne['Play'].PromoteAPawn(self.GameBoard, Position, Color)
            elif Color == self.BotNumTwo['Color']:
                self.GameBoard[Position[0]][Position[1]] = self.BotNumTwo['Play'].PromoteAPawn(self.GameBoard, Position, Color)

    def __Display__(self):
        for row in self.GameBoard:
            print(row)
        print('=========================================')

    """
    ---------------------------------
    help region setters
    """

    # set BotOne Name
    def SetBotOneName(self, Name):
        self.BotNumOne['Name'] = Name

    # set BotTwo Name
    def SetBotTwoName(self, Name):
        self.BotNumTwo['Name'] = Name

    """
    end of help region
    ---------------------------------
    """
