''' more abou functions arguments and  parameters '''
import math
# def welcome(name,msg):
#     print(f"Welcome {name} {msg}")

# welcome('Siva','Hi')

#arguments = postional and keyword arguments
# the parameter takes the values in the ordered way is called positional Arguments.(Default)
# name is the parameter and arugument given 


#Keyword arugument

# def welcome(name,msg):
#     print(f"Welcome {name} {msg}")

# welcome(msg ='Hi',name = 'Siva') # postion not matters here this way is keyword aruguments

" 001 finding the paint"

# wall_height = int(input('What is your wall height? '))
# wall_width = int(input('What is your wall wall_width? '))
# coverage =5

# def findcans(wh,ww,wc):
#     number_of_cans = (wh * ww) / wc
#     print(math.ceil(number_of_cans))

# findcans(wall_height,wall_width,coverage)

''' prime Number checker '''

# def prime_number(number):
#     is_prime = True
#     for i in range(2,number):
#        if number % i == 0:
#           is_prime = False
    
#     if is_prime:
#         print('It"s a prime number')
#     else:
#         print('not a prime number')

# num = int (input('What is the number? '))
# prime_number(number =num)


'''... caesar cipher ... '''


# encode decode challenge
alphabet = [
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def getcode (dir ,word , shift_num):
       getword=''
       for letter in word:
          current_pos = alphabet.index(letter)
          if dir == 'encode':
             new_pos = current_pos + shift_num
             encodelet =alphabet[new_pos]
             getword +=encodelet
          else:
             new_pos = current_pos - shift_num
             encodelet =alphabet[new_pos]
             getword +=encodelet

       print(getword)


getcode(direction,text,shift)