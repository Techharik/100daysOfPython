# ''' dictionary and nesting '''

# dictionary = object

# # Person = {
# #     'name' : 'Hari Prasath',
# #     'Age' : 22
# # }

# # print(Person)
# # print(Person['name']) #assging the data in the dictionary

# #key error - if the daya is not FileNotFoundError
# #Note - key also have  a '' else the key is consider as variable only for String
# # but for number you can us without '' example given below 👇
# Person = {
#     'name' : 'Hari Prasath',
#     'Age' : 22,
#     0:'poda'
# }


# print(Person)
# print(Person[0])


# #adding new item to dictionary:   👇

# Person['place']='odc'
# print(Person)

# #create a empty dictionary and wipe the previous dictionory:👇👇

# # Person ={}
# # print(Person)


# #edit a item in a dictionary🤚

# Person['place']='Kovai'

# print(Person)

# #loop in dictionary:

# for keys in Person:
#     print(keys) #enumaeration happening here
#     print(Person[keys]) # Getting the values in the Objects/ dictionaries.


# students_scores = {
#     'Harry':81,
#     'Ron':78,
#     'Hermione':99,
#     "Draco":74,
#     'Neville':62
# }


# for students in students_scores:
#     if students_scores[students] >= 91 and students_scores[students] <=100:
#         students_scores[students]='Outstanding'
#     elif students_scores[students] >= 81 and students_scores[students] <=90:
#         students_scores[students]='expectaions'
#     elif students_scores[students] >= 71 and students_scores[students] <=80:
#         students_scores[students]='Accceptable'
#     else:
#         students_scores[students] ='fail'

# print(students_scores)


''' Nesting '''

# Kovai ={
#     'locations':['saravanapatti','TechPark','kalapatti'],
#     'toruistplace': {
#         'ivistied':['ooty','polachi','siruli falls']
#     }
# }

# # print(Kovai['locations'][1])
# print(Kovai['toruistplace']['ivistied'][1])
import os


aution_biders = []


def auction_winner():
    for bidders in aution_biders:
        highest_bid =0
        if bidders['price'] > highest_bid:
            highest_bid = bidders['price']
            winner = bidders['name']
    print(f"The winner is {winner} the bid is {highest_bid}")


aution = True

print(aution)
while aution:
    name = input('What is your name? ')
    bid = int(input('What is your bid? '))

    def add_bider(name, price):
        aution_biders.append({
            'name': name,
            'price': price
        })
       
    add_bider(name, bid)
    continue_bid = input('what to continue the bid? ')

    if continue_bid == 'yes':
        os.system('clear')
    else:
       aution = False
       auction_winner()

