#import things
import os
from datetime import date

#def things
def sundays_from(start_date, end_date):
    number_of_sundays = 0
    for year in range(start_date, end_date + 1, 1):
        for month in range(1, 13):
            if date(year, month, 1).strftime("%A") == "Sunday":
                number_of_sundays += 1
    return number_of_sundays
os.system('cls' if os.name == 'nt' else 'clear')
start_date = int(input("Give me the starting year: "))
end_date = int(input("Give me the end year: "))
os.system('cls' if os.name == 'nt' else 'clear')
print(f"There are {sundays_from(start_date, end_date)} sundays that fall on the first of the month form January {start_date} to December {end_date}")