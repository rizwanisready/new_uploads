import datetime
from nptime import nptime

start_date = datetime.date(year= 2022, month=6, day=1)
end_date = datetime.date(year= 2022, month=6, day=5)
new_start_time = nptime(8, 0)
start_time = datetime.time(hour=8, minute=30, second=0)
end_time = datetime.time(hour=14, minute=30, second=0)
#print(start_time)
#print(end_time)
s = datetime.timedelta(minutes=30)
print(s)
dr_chauhan = []
while new_start_time < end_time:
    new_start_time = new_start_time + s
    dr_chauhan.append(str(new_start_time))
print(dr_chauhan,end="\n")


   