"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
and Fady Safwat
------------------------------------------------------------
summery:
this judge allows you to focus on choosing the best position to play
chess game Just by write your code in BotNumOne or BotNumTwo
"""
import ChessJudge
import BotNumOne, BotNumTwo
BotNumOneObj = BotNumOne.BotNumOne()
BotNumTwoObj = BotNumTwo.BotNumTwo()
Judge = ChessJudge.ChessJudge(BotNumOneObj, BotNumTwoObj)
Judge.SetBotOneName("Bot One")
Judge.SetBotTwoName("Bot Two")

Winner, GameBaord = Judge.TakeTurns()
print("Winner", Winner)
for row in GameBaord:
    print(row)
