import os
import datetime

def create_folders_between_dates():
    current_date = datetime.date.today()
    last_date = datetime.date(2026,12,31)
    list_of_dates = (last_date-current_date).days #list of dates between two dates


    for i in range(list_of_dates):
        current_date += datetime.timedelta(days=1) #day's Incress to one by one
        os.mkdir(f"C:/Users/hemanshu.marwadi/Desktop/Himanshu/OS_Module_Make_DIR/{current_date}")
          
create_folders_between_dates()


