"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
------------------------------------------------------------
summery:
this judge allows you to focus on choosing the best position to play
chess game Just by write your code in BotNumOne or BotNumTwo
------------------------------------------------------------
"""
import random
from Helper import *

class BotNumTwo:
    def play(self, GameBoard, Color):
        Army = GetArmy(Color, GameBoard)
        Enemy = GetArmy(GetEnemyColor(Color), GameBoard)
        """ choose piece randomly """
        Soldier = random.choice(Army)
        Row = random.randint(0, 7)
        Column = random.randint(0, 7)

        return Soldier['Position'], (Row, Column)

    def PromoteAPawn(self, GameBoard, Position, Color):
        return Color + Queen
