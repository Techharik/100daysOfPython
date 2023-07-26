# print('Day-5 Loops Range and code Blocks')

''' Average Height Calculator '''
# to demonstrate how loops iteration works in list  



# listHeight = input('Whhat is the list of height').split()

# avg = 0

# for height in listHeight:
#     avg += int(height)

# averageValue = round(avg/len(listHeight))

# print(averageValue)

#''' sum(array) -> returns a summ of list '''

 
''' Highest Score value founding in  a mark list '''


#marks = [78 , 65, 89, 86,55, 91, 64, 69,98]

#highest_value = 0
#for  mark in marks:
#   if(highest_value < mark):
#       highest_value = mark

#print(f'The highest value in the list is {highest_value}.🔥🔥')

#'''  max(array) -> returns the highest number in the list  '''
#'''  min(array) -> returns the lowest number in the list  '''


''' using for loop with range function '''
 #adding even numbers in 1 to 100:

# number = 0
# for num in range(2,101,2):
#     number +=num

# print(number)

#fizbuzz logic

# for num in range(1,101):
#     if(num % 5 == 0 and num % 3 == 0):
#         print('fizzbuzz')
#     elif(num % 5 == 0):
#         print ('buzz')
#     elif(num % 3 == 0 ):
#         print('fizz')
#     else:
#         print(num)


#password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#easy level

# str=''
# for letter in range(1,nr_letters+1):
#    str +=random.choice(letters)



# symbol=''
# for letter in range(1,nr_symbols+1):
#    symbol +=random.choice(symbols)


 
# number=''
# for letter in range(1,nr_numbers+1):
#    number +=random.choice(numbers)



# print(f'{str}{symbol}{number}')


#hard level

password_list= []
  
for letter in range(1,nr_letters+1):
   password_list.append(random.choice(letters))

for letter in range(1,nr_symbols+1):
   password_list.append(random.choice(symbols))

for letter in range(1,nr_numbers+1):
   password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(password_list) 

str=''

for passIn in password_list:
    str +=passIn

print(str)



''' summary '''

# loop:
# for passOur in arr:
#     print passOur

#range:

# for passOut in range(1,0,step):
#     print(passOut)

# random.choice(seq)-> takes a array and return random element in the array
#random.shuffle(seq)-> takes a arayy and suffle it doesn't return a new array
#array.append()-> used to add a element in the array

