import datetime
from nptime import nptime

start_date = datetime.date(year= 2022, month=6, day=1)
end_date = datetime.date(year= 2022, month=6, day=5)
s = datetime.timedelta(minutes=30)
t = datetime.timedelta(days=1)
new_start_time = nptime(8, 0)
#start_time = datetime.time(hour=8, minute=30, second=0)
end_time = datetime.time(hour=14, minute=30, second=0)
empty_list_date = []
empty_list_time = []

while start_date <= end_date:
    start_date = start_date + t
    
    empty_list_date.append(str(start_date))
    while new_start_time < end_time:
        
        new_start_time = new_start_time + s
        empty_list_time.append(str(new_start_time))
print(empty_list_date)
#print(empty_list_time)

