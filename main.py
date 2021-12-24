from _ml import MLAgent, train, save, load, train_and_plot, RandomAgent, validate, plot_validation
from _core import is_winner, opponent, start
import random
 


class MyAgent(MLAgent):
  def evaluate(self, board):
    if is_winner(board, self.symbol):
        reward = 1
    elif is_winner(board, opponent[self.symbol]):
      reward = -1
    else:
      reward = 0
    return reward

def parameters():
  print("Hyperparameters zijn parameters waarmee je de funcie en dus het gedrag van de machine-learning agent kunt aanpassen, in deze code worden twee hyperparameters gebruikt, alpha en epsilon \nAlpha: Deze parameter bepaald hoe snel de agent nieuwe kennis opneemt. Des te hoger alpha is, des the sneller de agent oude kennis zal vervangen voor nieuwe kennis \nEpsilon: Deze parameter bepaald hoe vaak de agent nieuwe zetten zal proberen, des te hoger dit getal, des te vaker de agent een random zet zal doen in plaats van de bekende beste zet   \nDe parameters moeten tussen de 1 en de 0 zijn")
  while True:
    try:
      chosen_alpha = float(input("alpha: \n"))
      chosen_epsilon = float(input("epsilon: \n"))
    except:
      print("kies getallen tussen 0 en 1 graag")
      continue
    else:
      if chosen_alpha <= 1 and chosen_epsilon <= 1:
        break
      else:
        print("kies getallen tussen 0 en 1 graag")
  
  my_agent = MyAgent(alpha=chosen_alpha, epsilon=chosen_epsilon)
  return my_agent



def choiche2():
  
  while True:
    play_agent = input("Tegen welke agent wil je spelen? Als je tegen de agent van dit programma wilt spelen, vul in: agent1, agent2 of agent3 \n")
    try:
      my_agent = load(play_agent)
    except:
      print("die agent bestaat niet, kies aub een andere")
      continue
    else:
      my_agent = load(play_agent)
      break
 
  my_agent.learning = False

  while True:
    play_symbol = input("Wil je x of o zijn? (x begint altijd) \n")
    if play_symbol == "x" or play_symbol == "X":
      start(player_o=my_agent) 
      break 
    elif play_symbol == "o" or play_symbol == "O":
      start(player_x=my_agent)
      break


def choice3():
  name = input("Hoe wil je dat je agent heet? \n")

  while True:
    try:
      training = int(input("hoe vaak moet je agent getraint worden? (max 50000) \n"))
    except:
      print("kies een getal graag")
      continue
    else:
      if training <= 50000:
        break

  print("wil je de hyperparameters aanpassen? (y/n)")
  if input() == "y":
    my_agent = parameters()
  else:
    my_agent = MyAgent()

  train(my_agent, training)
 
  save(my_agent, name)

  print("\nJe agent is getrain en gesaven onder: " + name)


def choice4():
  print("Als de grafiek getekend is, klik het weg om verder te gaan")

  while True:
    try:
      name = input("Hoe heet de agent \n")
      my_agent = load(name)
    except:
      print("deze agent bestaat niet")
      continue
    else:
      my_agent = load(name)
      break
  
  while True:
    symbol = input("Wil je dat jouw agent x of o is? (x begint altijd) \n")
    if symbol == "o" or symbol == "O" or symbol == "x" or symbol == "X":
      break
  
  my_agent.learning = False
 
  validation_agent = RandomAgent()

  if symbol == "x" or symbol == "X":
    validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)

  if symbol == "o" or symbol == "O":
    validation_result = validate(agent_o=my_agent, agent_x=validation_agent, iterations=100)

  plot_validation(validation_result)

def choice5():
  print("Als de grafiek getekend is, klik het weg om verder te gaan")

  random.seed(1)

  while True:
    try:
      itterate = int(input("How many itterations doe you want to do (max 50) \n"))
    except:
      print("kies een getal graag")
      continue
    else:
      if itterate <= 50:
        break

  my_agent = parameters()
  random_agent = RandomAgent()
 
  train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=itterate,
    trainings=100,
    validations=1000)


#1: 2 spelers
#2: speel tegen een al getrainde computer
#3: train een agent 
#4: plot piechart
#5: kijk welke hyperparameters de beste AI geven

while True:
  choice = input("\n 1: 2 spelers \n 2: speel tegen een getrainde computer \n 3: Train een AI \n 4: check hoe goed een bepaalde agent is \n 5: testen hoe goed bepaalde hyperparameter combinaties werken \n Kies wat je wilt spelen: \n")

  if choice == '1':
    start()

  if choice == '2':
    choiche2()

  if choice == '3':
    choice3()

  if choice == '4':
    choice4()

  if choice == "5":
    choice5()

  play = input("Wil je doorgaan? (y/n) \n")
  if play == 'y':
    continue
  else:
    break



