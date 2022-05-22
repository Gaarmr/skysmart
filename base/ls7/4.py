year1 = 1999
mon1 = 1
day1 =1

year2 = 1998
mon2 = 12
day2 = 31

if year1 < year2:
    print('первый старше по году')
elif year2 < year1:
    print('второй старше по году')
elif mon1 < mon2:
    print('первый старше по месяцу')
elif mon2 < mon1:
    print('второй старше по месяцу')
elif day1 < day2:
    print('первый старше по дням')
elif day2 < day1:
    print('второй старше по дням')
else:
    print('ровесники')
