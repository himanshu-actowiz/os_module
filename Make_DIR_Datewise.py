import os
import datetime

current_date = datetime.date.today()
last_date = datetime.date(2026,12,31)
list_of_dates = (last_date-current_date).days #list of dates between two dates

def create_folders_between_dates(current_date,last_date,list_of_dates):
    for i in range(list_of_dates):
        current_date += datetime.timedelta(days=1) #day's Incress to one by one
        os.mkdir(f"C:/Users/hemanshu.marwadi/Desktop/Make_DIR_Using_OS_Module/{current_date}")
          
create_folders_between_dates(current_date,last_date,list_of_dates)
    
    


    


