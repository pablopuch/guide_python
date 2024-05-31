### Fechas ###

import datetime
from datetime import datetime

now = datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.year)

timestamp = now.timestamp()
print(timestamp)


day = now.day                  
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute             
second = now.second
print(f'{day}/{month}/{year}, {hour}:{minute}')


def print_new_year(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
new_year = datetime(2050, 3, 11)

print_new_year(new_year)

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(2024, 4, 20)

print(current_date.year)
print(current_date.month)
print(current_date.day)

#Operaciones con fechas

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date)

from datetime import timedelta

init_timedelta = timedelta(200, 100, 100, weeks= 13)
end_timedelta = timedelta(300, 100, 200, weeks= 52)

print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)

'''
    No tiene mucho sentido multiplicar o dividir fechas.
'''
# print(end_timedelta * init_timedelta)
# print(end_timedelta / init_timedelta)
