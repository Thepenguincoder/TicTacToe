import random
from bke import EvaluationAgent, start

#class MyRandomAgent(EvaluationAgent):
 # def evaluate(self, board, my_symbol, opponent_symbol):
  #  return random.randint(1, 500)

class MyCapableAgent(EvaluationAgent):
  def getBoardCopy(board):
    boardCopy = []
    for i in board:
      boardCopy.append(i)
    return boardCopy

  
  
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = random.randint(1, 500)
    if board[4] == None:
      getal = 4
    return getal

#my_random_agent = MyRandomAgent()
my_agent = MyCapableAgent()
start(player_o = my_agent)
