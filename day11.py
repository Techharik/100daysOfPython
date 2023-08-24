print('Welcome to Day -11 Capstone Project');



''' BlackJack Number '''
import random


def chose_number(): 
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    random_card = random.choice(cards)
    return random_card

your_card = []
computer_card = []
game_ends = False;

for _ in range(2):
    your_card.append(chose_number())
    computer_card.append(chose_number())

print(f"your score is {your_card}")
print(f"your score is {computer_card[0]}")

def calulate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11).apend(1)

    return sum(cards)

score = calulate_score(your_card)

print(score)

if score > 21 or score == 0:
        game_ends = True
        print(f"Do you want to end the game")
  


