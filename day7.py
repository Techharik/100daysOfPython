''' Hangman Game '''
import random

word_list = ['ardvark', 'babbon', 'Camel']

# Todo:1 RANDAM CHOOSAN A WORD FROM THE word_list

random_number = random.randint(0, (len(word_list)-1))
# we can use random.choice()- to get a random words in the list

choose_word = word_list[random_number].lower()

print(choose_word)
game_word = []
for _ in range(len(choose_word)):
    game_word += '_'


end_of_game = False
level = len(choose_word)

while not end_of_game:
    guess_letter = input('Guess Letter: ').lower()
    for pos in range(len(choose_word)):
        letter = choose_word[pos]
        if letter == guess_letter:
            if game_word[pos] == '_':
               game_word[pos] = letter
            else:
                print('letter already exist')
        
    print(game_word)

    if guess_letter not in choose_word:
        level -= 1
        if level == 0:
            print('You Lose')
            end_of_game = True

    if "_" not in game_word:
        end_of_game = True
        print('You won')
