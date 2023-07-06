# print('Welcome to Day-2')

# Type casting or type converstion Practice !

# num = input('What is the two digit number?')

# str_num = str(num)

# num_1 = int(str_num[0]) + int(str_num[1])

# print(num_1)


# BMI Calculator;

# weight = int(input('What is your weight?'))
# height = float(input('What is your height?'))

# Bmi = weight / (height**2)

# print(int(Bmi))

# life week left - 90

# myAge = int(input('What is your age?'))

# year_left = 90 - myAge;

# month_left = year_left*12

# week_left = year_left*52

# days_left =year_left*365

# print(f'you have {days_left}days , {week_left}weeks , {month_left} months left  ')


# tip Calculator

total_bill = float(input('Wwhat is your total bill?'))

tip = int(input('What is your tip calculator 10, 12, and 24?'))

total_pay = (total_bill/100)*tip

split = int(input('Total number of split?'))

pay_each = round((total_pay+total_bill)/split, 2)

print(f'Each person should pay {pay_each} dollars')
