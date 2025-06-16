from datetime import date,time,datetime

today = date.today()
t = datetime.now()

print("the date is",today)
print("the time is",t)

print(f"{today.year}/{today.month}/{today.day}")