

age = int(input('Enter age:'))

if(age<2):
    print('person is baby')
elif (2 <= age < 4):
    print('person is toddler')
elif (4 <= age < 13):
    print('person is kid')
elif (13 <= age < 20):
    print('person is teenger')
elif (20 <= age < 65):
    print('person is adult')
else:
    print('person is elder')