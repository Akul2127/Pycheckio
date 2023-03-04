import datetime

today = datetime.date.today()
print(today)

birthday = datetime.date(2010, 12, 27)
print(birthday)

days_since_birth = (today-birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days=10)
print(today-tdelta)

print(today.day)
#saurday = 5
print(today.weekday())

#mon = 0, sun = 6
print(datetime.time(8, 45, 30))
hour_delta = datetime.timedelta(hours=12)