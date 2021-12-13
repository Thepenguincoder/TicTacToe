import random
from bke import EvaluationAgent, start, is_winner

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
    for i in range(0, len(board)):
      boardCopy = MyCapableAgent.getBoardCopy(board)
      if boardCopy[i] == ' ':
        boardCopy[i] = my_symbol
        if is_winner(boardCopy, my_symbol):
          return i

    for i in range(0, len(board)):
      boardCopy = MyCapableAgent.getBoardCopy(board)
      if boardCopy[i] == ' ':
        boardCopy[i] = opponent_symbol
        if is_winner(boardCopy, opponent_symbol):
          return i
    
    cornerMoves = [0,2,6,8]
    possibleMoves = []
    for i in cornerMoves:
      if board[i] == ' ':
        possibleMoves.append(i)
        if len(possibleMoves) != 0:
          return random.choice(possibleMoves)

    sideMoves = [1,3,5,7]
    possibleMoves = []
    for i in sideMoves:
      if board[i] == ' ':
        possibleMoves.append(i)
        if len(possibleMoves) != 0:
          return random.choice(possibleMoves)

    return random.randint(0,8)



#my_random_agent = MyRandomAgent()
my_agent = MyCapableAgent()
start(player_o = my_agent)