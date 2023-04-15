# Visit the Slack legacy tokens page. https://api.slack.com/legacy/custom-integrations/legacy-tokens
Scroll down to the “Legacy token generator” section and click on the “Create token” button next to the workspace you want to generate a token for. If you’re not already signed in to the workspace, you’ll be prompted to do so.
Once you’ve created the token, copy it and store it securely. Keep in mind that legacy tokens provide access to all data in a workspace and do not support granular permissions, so they should be treated like passwords and kept confidential.
To use the legacy token with the Slack API, include it as a bearer token in the Authorization header of your HTTP requests. For example, if you’re using Python and the requests library, you can make an authenticated request to the conversations.list method like this:

# import requests

headers = {
    'Authorization': 'Bearer YOUR_LEGACY_TOKEN'
}

response = requests.get('https://slack.com/api/conversations.list', headers=headers)

data = response.json()
This code sends an authenticated GET request to the conversations.list method of the Slack API using a legacy token. The token is included as a bearer token in the Authorization header of the request. The response is then parsed as JSON and stored in the data variable.

You can use this approach to make authenticated requests to any method of the Slack API that supports legacy tokens. Keep in mind that some methods may not support legacy tokens or may have limited functionality when used with them.


# can you explain what legacy tokens are to me like I'm 5 years old


Sure! Imagine you have a special key that can open all the doors in your house. You can use this key to go into any room 
you want and see what’s inside. But you have to be very careful with this key because if someone else gets it, 
they can also open all the doors in your house and see everything inside.
A legacy token is like that special key, but for Slack. It’s a special code that lets you see all the 
messages and information in your Slack workspace. You can use it to get information from Slack without having to log in every time. 
But you have to be very careful with it because if someone else gets it, they can also see all the information in your Slack workspace.
I hope this helps you understand what legacy tokens are! Let me know if you have any further questions.