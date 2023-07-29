''' Hangman Game '''
import random

word_list = ['ardvark', 'babbon', 'Camel']

# Todo:1 RANDAM CHOOSAN A WORD FROM THE word_list

random_number = random.randint(0, (len(word_list)-1))
# we can use random.choice()- to get a random words in the list

choose_word = word_list[random_number]

print(choose_word)

guess_letter = input('Guess Letter: ')

game_word = []
i = 0

while (i < len(choose_word)):
    if (guess_letter == choose_word[i].lower()):
        game_word.append(guess_letter)
    else:
        game_word.append('_')
    i += 1

print(game_word)
