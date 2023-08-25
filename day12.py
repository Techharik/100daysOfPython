''' namespace and scope '''

# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 2
#     print(f"enemies inside funtion:{enemies}")

# increase_enemies()
# print(f"enemies outside funtion:{enemies}")


''' Global scope is accessed by everyone but functional scope is accessed by only function: '''

#local scope - existed with in the function.
# access only inside the function not accessable by outside.

#Global scope - Pothu sothu.
 
#There is no Block Scope in python. - so loops and if declared variables are 
#not couted inside the intentation

''' modifiy the global scope '''

# using global keyword we can access the global variable.


#Global Constant: variabl enot coing to change written in uppercase , speration by _

#activate my brain to remeber that uppercase is never changeing one.

# PI = 3.14159


#guess the number:
# 23;
#guess leve - easy 10 - 5 times:

# if count - 10 - 

# loop - 5 times:

# slec

#if guees greater - two high;
#   count -1

# else - two lwo;

#eq

import random

def play():
    def choose_number():
        rand_number = random.randint(0,100)
        return rand_number

    chosed_number = choose_number()

    level = input('Type easy or hard:')
    game_count = 0

    if level == 'easy':
        game_count = 10
    elif level == 'hard':
        game_count = 5
    game_ends = False

    while not game_ends:
        if game_count !=0:
            guess_number = int(input(' What is your guess number?'))
            if guess_number < chosed_number:
                print('Too lwo')
                game_count =game_count - 1
                print(game_count)
            elif guess_number > chosed_number:
                print('Too High')
                game_count =game_count - 1
            else:
                print('you win')
                game_ends = True
        else:
            print('You Lose')
            play_again = input('Do you want to play again? y / n')

            if play_again == 'y':
                play()
            else:
                print('Bye')
                game_ends=True
                return



play()      
