import random
import os

first_list = [
    {
    'name':'neymar',
    'followers':100
    },
    {'name':'ronoldo','followers':200},
    {'name':'kyle','followers':300},
    {'name':'Tate','followers':400},
    {'name':'logonpaul','followers':500},

]

second_list = [
    {
    'name':'stalin',
    'followers':101
    },
    {'name':'vijay','followers':201},
    {'name':'capton','followers':301},
    {'name':'seman','followers':401},
    {'name':'ajith','followers':501},

]

person_1 = {}
person_2 = {}

def playagain():
    game_over = False
    points = 0

    while not game_over:
        def rand_chose():
            global person_1 ,person_2
            person_1 = random.choice(first_list)
            person_2 = random.choice(second_list) 
        rand_chose()
        print(f"The person 1 is {person_1['name']}   vs  person 2 is {person_2['name']}")
        guess = input('The given followers is higher or lower? h /l ')
        
        if guess == 'h':
            if person_1['followers'] > person_2['followers']:
                points +=1
            else:
                game_over =True
                os.system('clear')
                print(f'Your Point is {points}')
        else:
           if person_1['followers'] < person_2['followers']:
                    points +=1
           else:
                    game_over =True
                    os.system('clear')
                    print(f'Your Point is {points}')

playagain()   
