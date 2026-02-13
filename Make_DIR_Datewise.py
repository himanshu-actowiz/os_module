import os
from datetime import *

Current_date = input("Enter a CURRENT DATE : YYYY-MM-DD ")

def create_folders_between_dates(Current_date):   
    Convert_date_DATETIME = datetime.strptime(Current_date,"%Y-%m-%d")
    Current_Day_Number = Convert_date_DATETIME.timetuple().tm_yday
    Find_Remaning_Days = 365-Current_Day_Number + 1
    for i in range(1,Find_Remaning_Days):
        Increase_Date = Convert_date_DATETIME + timedelta(days=i)
        s = str(Increase_Date).split(" ")[0]
        os.mkdir(f"C:/Users/hemanshu.marwadi/Desktop/OS_MAKE_DIR/{s}")

create_folders_between_dates(Current_date)


