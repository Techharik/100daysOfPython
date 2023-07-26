# print('Day-5 Loops Range and code Blocks')

''' Average Height Calculator '''


listHeight = input('Whhat is the list of height').split()

avg = 0

for height in listHeight:
    avg += int(height)

averageValue = round(avg/len(listHeight))

print(averageValue)

''' sum(array) -> returns a summ of list '''
