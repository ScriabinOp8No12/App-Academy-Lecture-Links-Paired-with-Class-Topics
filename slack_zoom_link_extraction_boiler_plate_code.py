import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="YOUR_SLACK_API_TOKEN")

try:
    # Call the conversations.history method using the WebClient
    result = client.conversations_history(channel="YOUR_CHANNEL_ID")
    messages = result['messages']
    # Extract Zoom links from messages
    zoom_links = []
    for message in messages:
        text = message['text']
        links = re.findall(r'(https://\S*?zoom.us\S*)', text)
        zoom_links.extend(links)
    print(zoom_links)
except SlackApiError as e:
    print(f"Error: {e}")

# Slack API and the Google Drive API info:
#
# Use the Slack API to retrieve messages from a specific channel and then use regular expressions to extract Zoom links
# from those messages. Once you have the links, you can use the Google Drive API to create a new document and
# write the links to it.
#
# You can use the slack-sdk library to interact with the Slack API 1.
# You can also use the google-api-python-client library to interact with the Google Drive API 2.
