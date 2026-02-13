# import os
# import datetime

# current_date = datetime.date.today()
# last_date = datetime.date(2026,12,31)
# list_of_dates = (last_date-current_date).days #list of dates between two dates

# def create_folders_between_dates(current_date,last_date,list_of_dates):
#     for i in range(list_of_dates):
#         current_date += datetime.timedelta(days=1) #day's Incress to one by one
#         os.mkdir(f"C:/Users/hemanshu.marwadi/Desktop/Make_DIR_Using_OS_Module/{current_date}")
          
# create_folders_between_dates(current_date,last_date,list_of_dates)
    
import os
from datetime import *

Current_date = input("Enter a CURRENT DATE : YYYY-MM-DD ")

def create_folders_between_dates(Current_date):   
    Convert_date_DATETIME = datetime.strptime(Current_date,"%Y-%m-%d")
    Current_Day_Number = Convert_date_DATETIME.timetuple().tm_yday
    Find_Remaning_Days = 365-Current_Day_Number + 1
    for i in range(Find_Remaning_Days):
        Increase_Date = Convert_date_DATETIME + timedelta(days=i)
        s = str(Increase_Date).split(" ")[0]
        os.mkdir(f"C:/Users/hemanshu.marwadi/Desktop/OS_MAKE_DIR/{s}")

create_folders_between_dates(Current_date)


