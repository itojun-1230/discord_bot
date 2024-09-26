import sys
import requests

args = sys.argv
botToken = args[1]
channelId = args[2]

url = f"https://discord.com/api/v10/channels/{channelId}/messages"
headers = {
    "Authorization": f"Bot {botToken}",
    "Content-Type": "application/json",
}
payload = {
    "content": "Hello, World!",
}
r = requests.post(url, headers=headers, json=payload)

print(r.text)