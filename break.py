month =int(input('enter a month (as integer)'))
day=1

while day <= 31:
    if month == 2 and day > 28:
        break
    if(month == 4 or month == 6) and day>30:
        day +=1
        continue
    print(day)
    day +=1
