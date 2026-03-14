# A program To generate Date For 1st  Vaccination
import random
from datetime import date, timedelta

def vaccination_dates():
    # Start date set to Jan 1st, 2020
    start_date = date(2020, 1, 1)
    end_date = date.today()
    
    # Generate a valid random date for the 1st dose
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates + 1)
    dose1_date = start_date + timedelta(days=random_number_of_days)
    edate = dose1_date.strftime("%d-%m-%Y")

    # Calculate 2nd dose date
    day_diff = random.choice([28, 84])
    dose2_date = dose1_date + timedelta(days=day_diff)
    confirm_date = dose2_date.strftime("%d-%m-%Y")
    
    return [edate, day_diff, confirm_date]

if __name__ == "__main__":
    edate, day_diff, confirm_date = vaccination_dates()
    print(f"1st Dose Date: {edate}")
    print(f"Day Gap: {day_diff}")
    print(f"2nd Dose Date: {confirm_date}")