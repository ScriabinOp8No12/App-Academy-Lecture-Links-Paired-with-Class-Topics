
**** Explanation of the code ****

This code uses BeautifulSoup to parse the HTML of the web page you’re trying to extract information from.
It finds all the h3 elements with class 'sc-dnqmqq kcAQXs' using the find_all method and stores them in the
h3_elements variable. It then creates a dictionary called days where the keys are the days of the week and the
values are lists of topics for that day. The valid_days list specifies which days you’re interested in extracting
topics for and the not_valid_topics list specifies which topics to exclude.

The code iterates over the h3_elements and checks if their text is one of the valid days specified in the
valid_days list. If it is, it sets the current_day variable to be the text of the h3_element and creates a new entry
in the days dictionary for that day. It then finds the next ul element after the current h3_element using the
find_next method. If it finds a ul element, it finds all the li elements within it using the find_all method and
iterates over them. For each li element, it finds a header element with class 'sc-gqjmRU kvshPl' within it using the
find method. If it finds a header element and its text is not in the not_valid_topics list, it appends its text to
the list of topics for the current day.


*************** My original plan, was off a little bit ************

Start at the upper most h3 element. Start a loop to go through all the h3 elements.
If the text value of the h3 element is not Monday, Tuesday, Wednesday, Thursday, or Saturday, then break.
If it is one of those days, then

 find the next ul element after the current h3_element using the find_next method
 If it finds a ul element, it finds all the li elements within it using the find_all method and iterates over them.
 For each li element, it finds a header element with class 'sc-gqjmRU kvshPl' within it using the find method.
 If it finds a header element and its text is not in the not_valid_topics list,
 it appends its text to the list of topics for the current day.

store all of the header elements with class 'sc-gqjmRU kvshPl' text values
in a dictionary as values (use a list for the values) with the h3 element as the key.
for the starting one, that would be Monday as the key, with values of the heading element with class
elements with class 'sc-gqjmRU kvshPl' which is {'Monday', ['Orientation', Skills Survey']
now since it finished finding all those heading elements, it starts over at the next h3 element in the loop.

***********************************************************************************************************

My original code block below to print everything out


h3_elements = each_day_doc.find_all('h3', class_=['sc-dnqmqq kcAQXs', 'sc-dnqmqq jLQnpZ'])
for h3_element in h3_elements:
    print('days:', h3_element.text)
# Get the topic elements from the updated doc object -> these are TOPICS
topic_elements = each_day_doc.find_all('header', class_='sc-gqjmRU kvshPl')
for topic_element in topic_elements:
    # valid topics
    if topic_element.text not in not_valid_topics:
        print("topics:", topic_element.text)
this code block above prints out all the days and topics

print(each_day_doc)

***********************************************************************************************