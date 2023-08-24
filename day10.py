''' Functions with Outputs'''

# def add_values(num1,num2):
#     return num1 + num2

# Output = add_values(4,5)
# print(Output)


# .title() - Captiliazion of the word
# Doc String- Documentation for writing String.
#   First line of our coustom function use ''' ''' to write documentation string.

''' Docus String '''
import os

def add_values(num1, num2):
    ''' Our_Function '''
    return num1 + num2


Output = add_values(4, 5)
print(Output)

# Calculator:


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

continue_opp = True

final_result = 0


num1 = float(input('What is your first Number ? '))

while continue_opp:

    for operator in operations:
        print(operator)

    choosen_operator = input('What kind of operation you need to do ?')

    run_operation = operations[choosen_operator]

    num2 = float(input('What is your second number ?'))

    result = run_operation(num1, num2)

    print(f'{num1} {choosen_operator} {num2} = {result}')
    final_result = result

    continue_fun = input('Do you what to continue the operation ? y/n')

    if (continue_fun != 'y'):
        continue_opp = False
        os.system('clear')
    else:
        num1 = result
        os.system('clear')
        print(f'your result is {num1}')


print(f'{num1} {choosen_operator} {num2} = {final_result}')


#recursion a function calling himself: