import sys
import requests

args = sys.argv
botToken = args[1]
channelId = args[2]
gasURL = f"https://script.google.com/macros/s/AKfycbwM8MkxtgbiBhKnlge2HmV1TodCc6woucUJ_wJXaiLcG-YNsgEt6NtYhYkcaH3q_xl1/exec"

def main():
  messageData = getMessageData()
  messageId = messageData["messageId"]

  yes_users = getReactions(botToken, channelId, messageId, "⭕")
  no_users = getReactions(botToken, channelId, messageId, "❌")

  print(yes_users)
  print(no_users)



def getMessageData():
  r = requests.get(gasURL)
  return r.json()

def getReactions(botToken, channelId, messageId, reaction):
  url = f"https://discord.com/api/v10/channels/{channelId}/messages/{messageId}/reactions/{reaction}"
  headers = {
    "Authorization": f"Bot {botToken}",
    "Content-Type": "application/json",
  }
  r = requests.get(url, headers=headers)

  users = []
  for user in r.json():
    users.append(user["username"])
  return users

main()