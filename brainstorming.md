1. Check lecture (zoom link) posted date and time using slack API
2. If it's posted after 11pm but before midnight, that must be that current date's lecture (VERY RARE, probably 0%)
3. If lecture posted before the next day's starting class (8pm) then the lecture must be from the previous day
4. Edge cases 1: If lecture posted before 11pm Thursday and 10am Saturday, that must be Thursday's lecture, since we don't
have class on Fridays
5. Edge case 2: If lecture posted between 4:30pm Saturday and 8pm Monday, that must be Saturday's lecture because we don't
have class on Sundays
6. Holidays will mess us up.  There was no class for an entire week during Spring Break in March, so the class material
associated with that lecture would all be off a week if we don't use some conditionals here
7. Manually input the holiday dates, so that we can associate week 12's material (week of Spring Break) with the week after
8. Basically, if there's a holiday week, don't increment the week and day count when figuring out what material is on the lecture

Given these lectures -> we now know which date or which class they were from.

Also, here's the thought process for getting the week and day number given our current date

1. Set our cohort's starting date to January 9th, 2023.  That will be associated with Week 1 Day 1
2. Now if a lecture link is found with a certain date, like January 12th, 2023, we know that that was from class 
on January 11th, 2023, which is 2 days after our start, which means we are on Week 1, Day 3.  Now we go to Week 1, Day 3
on App Academy Open and scrape all the associated titles of the material we went over on that day. 
3. Now we have the material of that day, and the associated zoom link, we store these as key value pairs and then
add them to google drive with the following columns / data

   1. Date of lecture
   2. Lecture topic of that week
   3. Specific lecture topic for that day 
   4. Zoom link 
   5. Zoom link password


Boilerplate code from ChatGPT4:
I asked it what week and day March 15th would be, and it correctly told me it was Week 10, day 3:

from datetime import datetime

start_date = datetime(2023, 1, 9)
# Plug in March 15th into the current_date below
current_date = datetime(2023, 3, 15)

delta = current_date - start_date
days = delta.days

week = days // 7 + 1
day = days % 7 + 1

print(f"Week {week}, Day {day}")
# Output is Week 10, Day 3   Which is correct!

-----------------------------------------------------------

# Issue is we need to subtract one from the posted lecture date nearly 100% of the time, so here's 
# the new code it gave me, I haven't tested it yet

from datetime import datetime, timedelta

start_date = datetime(2023, 1, 9)
lecture_dates = [datetime(2023, 1, 10), datetime(2023, 1, 12), datetime(2023, 1, 17)]

for lecture_date in lecture_dates:

# Lecture was posted one day after the class
    class_date = (lecture_date - timedelta(days=1)).date()

    delta = class_date - start_date.date()
    days = delta.days
    week = days // 7 + 1
    day = days % 7 + 1

# {lecture_date.strftime('%Y-%m-%d')} is a Python string formatting expression that converts a datetime object into 
# a string representation of the date in the format YYYY-MM-DD. For example, if lecture_date is equal 
# to datetime(2023, 1, 10), then lecture_date.strftime('%Y-%m-%d') would return the string '2023-01-10'.
    
print(f"Lecture on {lecture_date.strftime('%Y-%m-%d')} corresponds to class on {class_date} (Week {week}, Day {day})")



