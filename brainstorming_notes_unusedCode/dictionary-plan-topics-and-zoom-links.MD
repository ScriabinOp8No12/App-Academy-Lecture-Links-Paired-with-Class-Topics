Plan for how to pair the zoom links up with the correct topics
# Use key value storage, and then use a pandas dataframe to export to google sheets?

google sheet api is fun -> good skill to have

1. Store the app academy topics into a string version of a key as "week1day1" (use a dictionary -> never used one in Python before)

2. Store these topics with values of all the topics covered (we can have multiple values for the same key right?)
Example:  From week 1, selenium scrapes the topics from Monday, which gets converted into day 1, with week 1, so the entire
string is week1day1.  Then selenium takes all the topics it scraped from that Monday and stores it as a value for this key

immutable dict (if it's comma separated) -> different syntax
1 to 1 key to value pair would work better!
Overall output would look like this:  {'week1day1': 'orientation, environment setup, program details'}

3. Remember that Friday will sometimes have topics, but we don't have lectures for that or go over it, however,
we probably need to include it because otherwise our week and day number will get messed up using our zoom date conversion.

# Basically, use a loop and search for the keywords (probably need to HARDCODE the day numbers here to avoid edge cases!)
Monday = day1
Tuesday = day2
Wednesday = day3
Thursday = day4
Friday = day5
Saturday = day6

Now, when we do the following conversion of the Zoom lecture date to the week and day number, it'll match up with the 
topics covered on that day.  

4. The Zoom lecture date will need to be converted to a string, so if plugging in March 15th, 
code would output Week 10, day 3, convert that to a string of week10day3.

5. Match that string to the key that we have for the topics, then store all of that into a new 'FINAL' dictionary
Example: Since March 15th has a zoom lecture, we convert that date into week10day3, then search for a key of week10day3 
in our app academy topics dictionary.  Once we find it, we take the values found from app academy topics, and use that as the new values,
then we make the key the zoom link + password.

# Final output would then be: {zoom.us/rec/share (AND PASSWORD HERE SOMEHOW -> maybe have this as a value too): 'week1day1, orientation, environment setup, program details'}

6. Use the google drive api to format these nicely and have an output that looks like this:

   1. Date of lecture, and main lecture topics of that week
   2. Specific lecture topics for that day 
   3. Zoom recording link and password