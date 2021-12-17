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


#1: 2 spelers
#2: speel tegen een al getrainde computer
#3: train een agent 
#4: plot piechart
#5: kijk welke hyperparameters de beste AI geven
itterate = 150
training = 500000
play = "y"
while play == "y":
  print("\n 1: 2 spelers \n 2: speel tegen een getrainde computer \n 3: Train een AI \n 4: check hoe goed een bepaalde agent is \n 5: testen hoe goed bepaalde hyperparameter combinaties werken \n Kies wat je wilt spelen: \n")
  choice = input()


  if choice == '1':
    start()

  if choice == '2':
    print("Tegen welke agent wil je spelen? Als je tegen de agent van dit programma wilt spelen, vul in: agent1")
    play_agent = input()


    my_agent = load(play_agent)
 
    my_agent.learning = False
 
    start(player_x=my_agent)    

  if choice == '3':
    print("Hoe wil je dat je agent heet?")
    name = input()

    while training >= 50000:
      print("hoe vaak moet je agent getraint worden? (max 50000)")
      training = int(input())

    print("wil je de hyperparameters aanpassen? (y/n)")
    if input() == "y":
      print("uitleg hyperparameter enzo, tussen 1 en 0")
      chosen_alpha = float(input())
      chosen_epsilon = float(input())
      my_agent = MyAgent(alpha=chosen_alpha, epsilon=chosen_epsilon)
    else:
      my_agent = MyAgent()

    train(my_agent, training)
 
    save(my_agent, name)

    print("\nJe agent is getrain en gesaven onder: " + name)

  if choice == '4':
    print("Als de grafiek getekend is, klik het weg om verder te gaan")

    print("Hoe heet de agent")
    name = input()
    print("Wil je dat jouw agent x of o is? (x begint altijd)")
    symbol = input()

    my_agent = load(name)
    my_agent.learning = False
 
    validation_agent = RandomAgent()

    if symbol == "x" or symbol == "X":
      validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)

    if symbol == "o" or symbol == "O":
      validation_result = validate(agent_o=my_agent, agent_x=validation_agent, iterations=100)

    plot_validation(validation_result)


  if choice == "5":
    print("Als de grafiek getekend is, klik het weg om verder te gaan")

    random.seed(1)
  
    print("uitleg hyperparameter enzo, tussen 1 en 0")
    print("alpha:")
    chosen_alpha = float(input())
    print("epsilon:")
    chosen_epsilon = float(input())

    while itterate >= 51:
      print("How many itterations doe you want to do (max 50)")
      itterate = int(input())

    my_agent = MyAgent(alpha=chosen_alpha, epsilon=chosen_epsilon)
    random_agent = RandomAgent()
 
    train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=30,
      trainings=itterate,
      validations=1000)

  print("do you want to continue? (y/n)")
  play = input()



