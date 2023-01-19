month = int(input())

if month == 12:
    print('winter')
elif month >= 3 and month < 6:
    print('spring')
elif month >= 6 and month < 9:
    print('summer')
else:
    print('fall') if (month >= 9 and month < 12) else print('winter') 