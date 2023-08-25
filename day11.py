print('Welcome to Day -11 Capstone Project')



''' BlackJack Number '''

import random

def play_game():
    def chose_number(): 
        cards = [11,2,3,4,5,6,7,8,9,10,10,10]
        random_card = random.choice(cards)
        return random_card

    your_card = []
    computer_card = []
    game_ends = False

    for _ in range(2):
        your_card.append(chose_number())
        computer_card.append(chose_number())

    while not game_ends:
        def calulate_score(cards):
            
            if sum(cards) == 21 and len(cards) == 2:
                return 0

            if sum(cards) > 21 and 11 in cards:
                cards.remove(11).apend(1)

            return sum(cards)

        your_score = calulate_score(your_card)
        computer_score = calulate_score(computer_card)

        print(your_score)
        print(computer_score)

        if your_score > 21 or your_score == 0 or computer_score == 0:
            if computer_score == 0 or your_score > 21:
                print('Computer Wins')
                game_ends = True
            elif computer_score == your_score:
                print('Draw')
                game_ends =True
            else:
                game_ends = True
                print(f'You win {your_score}')
                print("Do you want to end the game?")
        else:
            user_deal_card = input('Type y if you want to deal a another card?')
            if user_deal_card == 'y':
                your_card.append(chose_number())
            else:
                game_ends = True
                if your_score > computer_score and your_score <= 21:
                    print('You win.')
                elif computer_score == your_score:
                    print('Draw')
                    game_ends =True
                else:
                    print('Deck Wins')
                    Play_again = input('Do you want to play the game gain?')
                    if Play_again == 'y':
                        play_game()
                    else:
                        print('Bye')


   

play_game()
