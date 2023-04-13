# The python file will scrape the lecture topics from App Academy Open
# Store these lecture topics as the keys, and store the zoom links + password as the value
# Initially, we will have to store these lecture topics separated in a list

# Interesting observations: we will need to use selenium webdriver because the page is dynamically loaded with JS
# The URLs of each page don't seem to be visible when we use inspect so here's the pattern!

# 1. Go to this link to start: https://open.appacademy.io/learn/js-py---pt-jan-2023-online/
# 2. Scrape all the weeks with a string that contains Week + DOES NOT contain 'ASSESSMENT'
# 3. The info is stored in a li: <li class="sc-kpOJdX jPCnwj">Week 1-2 Assessment</li>
# 4. GENERATE PROPER LINKS TO SCRAPE
    # 1. Format goes:
         # week-1
         # three dashes ( --- ) because a hyphen follows the week everytime
         # title of week (in lowercase)
         # commas become single dash: -
         # spaces become single dash: -
         # and becomes two dashes: --
         # vs. becomes two dashes: --
         # dashes become three dashes: ---

    # 2. Edge cases:
         # Looks like week 15: Week 15 - HTTP, REST, and Servers
         # has the word 'and' near the end, but the page url uses only a single hypen
         # link to page is: https://open.appacademy.io/learn/js-py---pt-jan-2023-online/week-15---http--rest--and-servers/
         # ******** However, even if we use the following link (with two dashes for the 'and'), chrome fixes it
         # https://open.appacademy.io/learn/js-py---pt-jan-2023-online/week-15---http--rest--and--servers/

# *************** 2nd Method ****************:
# Figure out how to get selenium webdriver to click on the link itself, then scrape that link.  I'm told this is very
# challenging because the bot has to go back to the main link, I'm confused as to why this is hard?  Maybe it's
# cause there are multiple threads going at once, and that's hard to balance?
