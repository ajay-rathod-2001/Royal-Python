# A program To generate Date For 1st  Vaccination
import random, re,datetime
from datetime import date, timedelta

def vaccination_dates():
    current_year =date.today().year
    d = random.randint(1,31)
    m = random.randint(1,12)
    y = random.randint(2020,current_year)
    if y%4==0:
        if m==2:
            if d>29:
                d = random.randint(1,29)
        if y % 4!=0:
            if m == 2:
                if d>28 :
                    d = random.randint(1,28)  
        if m==4 or m==6 or m==9 or m==11:
            if d>30:
                d = random.randint(1,30)
gDate = str(y)+"-"+str(m)+"-"+str(d)
edate = re.sub(r"\d{4}-(\d{1,2})-(\d{1,2})","\\3-\\2-\\1",gDate)
gap = [28,84]
l = len(gap)
day_diff = gap[random.randint(0,l-1)]
ngDate = datetime.datetime(y,m,d) 
    
scheduled_day = ngDate + timedelta(days=day_diff) 
s_day = scheduled_day.day
s_months = scheduled_day.month
s_year = scheduled_day.year

next_sch_day = str(s_day)+"-"+str(s_months)+"-"+str(s_year)
confirm_date = re.sub(r"\d{4}-(\d{1,2})-(\d{1,2})","\\3-\\2-\\1",next_sch_day)     
return [edate,day_diff,confirm_date]

edate,day_diff,confirm_date= vaccination_dates()
print(edate)
print(day_diff)
print(confirm_date)