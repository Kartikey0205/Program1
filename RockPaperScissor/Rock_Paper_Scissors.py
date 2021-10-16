import random

OPTIONS = [0, 1, 2]

DISPLAY_SYMBOLS = {
    'rock': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'scissors': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
'paper': '''2
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''}

def player1Wins(choice1: str, choice2: str) -> bool:
    return (choice1 == 'rock' and choice2 == 'scissors') or (choice1 == 'scissors' and choice2 == 'paper') or (choice1 == 'paper' and choice2 == 'rock')

def getResult(choice1:str, choice2: str) -> str:
    if choice1 == choice2:
        return "It's a Draw.\n"
    if player1Wins(choice1, choice2):
        return "Player 1 wins this round!\n"
    return "Player 2 wins this round!\n"

def display(choice1: str, choice2: str):
    print(f"Player 1 chose - {choice1}")
    print(DISPLAY_SYMBOLS[choice1])
    print(f"Player 2 chose - {choice2}")
    print(DISPLAY_SYMBOLS[choice2])

def getKey(choice: int, symbols: dict) -> str:
    for key, value in symbols.items():
        if value == choice:
            return key

def playerSymbols():
    symbols= {}
    symbols['rock'] = random.choice(OPTIONS)
    temp = random.choice(OPTIONS)
    while temp == symbols['rock']:
        temp = random.choice(OPTIONS)
    symbols['paper'] = temp
    symbols['scissors'] = (set(OPTIONS) - set(symbols.values())).pop()
                          
    return symbols

def play() -> list[int]:
    willing = 'y'
    points1 = 0
    points2 = 0
    while willing == 'y':
        player1 = playerSymbols()
        print(player1)
        choice1 = getKey(int(input("Enter your choice: ")), player1)
    
        player2 = playerSymbols()
        print(player2)
        choice2 = getKey(int(input("Enter your choice: ")), player2)
    
        display(choice1, choice2)
        if player1Wins(choice1, choice2):
            points1 += 1
        else:
            points2 += 1

        print(getResult(choice1, choice2))

        willing = input("Do you want to continue? y/n -> ")
    
    return [points1, points2]
    

result = play()
if result[0] > result[1]:
    print("Player 1 has won the game!!")
elif result[0] < result[1]:
    print("Player 2 has won the game!!")
else:
    print("It's a draw between the 2 players!!")