# A program To generate Date For 1st  Vaccination
import random, re, datetime
from datetime import date, timedelta

def vaccination_dates():
    current_year = date.today().year
    d = random.randint(1, 31)
    m = random.randint(1, 12)
    y = random.randint(2020, current_year)
    
    # Validate day based on month and leap year
    if y % 4 == 0:
        if m == 2:
            if d > 29:
                d = random.randint(1, 29)
    else:
        if m == 2:
            if d > 28:
                d = random.randint(1, 28)
    
    if m in [4, 6, 9, 11]:
        if d > 30:
            d = random.randint(1, 30)
    
    # Create first vaccination date
    ngDate = datetime.datetime(y, m, d)
    
    # Calculate scheduled date with random gap (28 or 84 days)
    gap = [28, 84]
    day_diff = random.choice(gap)
    scheduled_day = ngDate + timedelta(days=day_diff)
    
    # Format the scheduled date as DD-MM-YYYY
    confirm_date = f"{scheduled_day.day:02d}-{scheduled_day.month:02d}-{scheduled_day.year}"
    return [edate,confirm_date]
cy = vaccination_dates()
print(cy)