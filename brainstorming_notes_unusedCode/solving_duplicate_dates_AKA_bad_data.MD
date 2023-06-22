Idea/plan:

Even after sorting, the same dates stay in the same position, so we can run one more filter at the very end that removes
any of the rows after the first time that date shows up. For example, if there are 3 May 5ths, find the row with the lower row number
and then delete all the other rows

OR just use some logic that says, if the date is the same as the current one you are on, DO NOT ADD IT to the Google Sheets!

Implementation (slightly different than original plan) -> USE A SET!  

Be careful not to run the program until after all the lecture recordings have been sent to GMAIL
A huge mistake would be to run the program at let's say 5pm, when there's one dud lecture, then the real lecture that comes in after
11:30pm MT won't be added to the Google sheets because the first one is in the set and the new one will not get added to the Google Sheets


Next steps:

ALSO need to delete the Friday and Sunday lecture dates.
Could also add the day of the week on the far left, just left of the date