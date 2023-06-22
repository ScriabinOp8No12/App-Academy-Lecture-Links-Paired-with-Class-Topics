# Steps:
# 1. Go to run, edit configurations,
# 2. Hit the plus button to create a new configuration
# 3. Click environment, and then environment variables
# 4. Add the name and value there
# 5. Add the script path (which is the path to this python file) with NO QUOTES at the start and end
# 6. Profit

import os

password_value = os.environ.get('APP_ACADEMY_PASSWORD')
print(password_value) # IT FINALLY WORKED! WOW
