import random
import my_module
# print('Day4')


# importing internal module and using;

# print(my_module.pi)

''' Randomaization in python and import internal and external modules'''
# Dice Functionality

# import random

# value = random.randint(0, 1)

# if value == 0:
#     print('Head')
# else:
#     print('Tails')


''' Lists In Python '''

# Bill PayGame in Landon

# business_names = 'Hari, Sabari, Siva, Vijay'

# members = business_names.split(',')

# # print(len(members))

# random_pick = random.randint(0, (len(members)-1))

# print(f'{members[random_pick]} is going to pay the bills')


# placeing the values task;

# row1 = ['', '', '']
# row2 = ['', '', '']
# row3 = ['', '', '']

# map = [row1, row2, row3]

# print(f'{row1},\n{row2},\n{row3}')

# value = input('What is t your position?')

# vertiacal = int(value[0])
# horizontal = int(value[1])

# map[vertiacal-1][horizontal-1] = 'x'

# print(f'{row1},\n{row2},\n{row3}')


# rock paper scissor game;
# 0 1 2

val = ['R', 'P', 'S']

your_num = int(input('What is your Number 0,1 or 2?'))

com_number = random.randint(0, 2)

if your_num <= 2 and com_number <= 2:
    if your_num == com_number:
        print(f' Draw,y{val[your_num]} ,c{val[com_number]}')
    elif your_num == 0 and com_number == 1:
        print(f'Computer win,y{val[your_num]} ,c{val[com_number]}')
    elif your_num == 1 and com_number == 2:
        print(f'Computer win,y{val[your_num]} ,c{val[com_number]}')
    elif your_num == 2 and com_number == 0:
        print(f'Computer win,y{val[your_num]} ,c{val[com_number]}')
    else:
        print(f'You win,y{val[your_num]} ,c{val[com_number]}')
else:
    print('Invalid Syntax')
