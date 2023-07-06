# print('Welcome to Day-3')
print('Conditional statement , logical Operator , code blocks and Scope')

# odd or evan calculator:

# number = int(input('What is the number?'))

# if number%2 == 0:
#     print('The given number is Even')
# else:
#     print('The Given number is Odd')


# Updated BMI Calculator:

# weight = int(input('What is your weight?'))
# height = float(input('What is your height?'))

# Bmi = round(weight / (height**2))

# print(Bmi)

# if Bmi < 18.5:
#     print('You have a lean Body')
# elif Bmi < 25:
#     print('You have a normal weight')
# elif Bmi < 30:
#     print('you ahve  a overweight')
# elif Bmi < 35:
#     print('you have a obese')
# else:
#     print('You are going to die')


# leap year checking

# year = int(input('What is the year?'))

# if year%4 == 0:
#     if year%100 !=0:
#       print('This is  a leap year')
#     else:
#         if year%4 ==0:
#             print('This is a Leap Year')
#         else:
#             print('This is not a leap Year')

# else:
#     print('This is not  a leap year')

# pizza ordering system:

# pizza_size = input('What is the size of your pizza S , M AND L ')

# price = 0
# if pizza_size == 'S':
#     price = 15
# elif pizza_size == 'M':
#     price = 20
# elif pizza_size == 'L':
#     price = 25
# else:
#     print('Invalid Size Selected')

# pepronni = input('Do you want pepronini? type Y or N')

# if pepronni == 'Y':
#     price += 2
# elif pepronni == 'N':
#     print('Pizza without pepronini is preparing')
# else:
#     print('Invalid Input')

# cheese = input('Do you want cheese? type Y or N')

# if cheese == 'Y':
#     price += 3
# elif pepronni == 'N':
#     print('Pizza without cheese is preparing')
# else:
#     print('Invalid Input')

# # extra cheese for any size pizza;
# extra_cheese = input('Do you want extra cheese? Type Y OR N ')
# price += 1

# print(f"You total bill is {price}")


# Tresure Game:

print('Welcoe to the Treasure Game')

direction = input('left of right? ')

if direction == 'right':
    print('Game Over')
elif direction == 'left':
    move = input('swim of wait? ')
    if move == 'swim':
        print('Game over')
    elif move == 'wait':
        print('you reached the island')
        color = input('Choose your color red,yellow,green ')
        if color == 'red':
            print('You set the fire to island, you dies')
        elif color == 'yellow':
            print('You won the Game')
        elif color == 'green':
            print('You are entered to monster room , you died')
        else:
            print('Invalid Input')
    else:
        print('Invalid Input')
else:
    print('Invalid direction')
