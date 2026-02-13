import os
import datetime

now = datetime.date.today()
f_date = datetime.date(2027,1,1)
list = (f_date-now).days
# print(list)

for i in range(list):
    now += datetime.timedelta(days=1)
    print(now)
    os.mkdir(f"C:/Users/hemanshu.marwadi/Desktop/Himanshu/{now}")
# # print(f_date)
# print(now)