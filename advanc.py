import calendar

print('Print a calendar for a year and month:')
month = int(input('Month (mm): '))
year = int(input('Year (yyyy): '))
print('\n')

calendar.setfirstweekday(calendar.SUNDAY)
cal = calendar.monthcalendar(year, month)

if len(str(month)) == 1:
    month = '0%s' % month

# Header
print('|++++++ %s-%s +++++|' % (month, year))
print('|Su Mo Tu We Th Fr Sa|')
print('|--------------------|')

# display calendar
border = '|'
for week in cal:
    line = border

    for day in week:
        if day == 0:
            # 3 spaces for blank days
            line += '   '
        elif len(str(day)) == 1:
            line += ' %d ' % day
        else:
            line += '%d ' % day
    # remove space in last column
    line = line[0:len(line) - 1]
    line += border
    print(line)

print('|--------------------|\n')