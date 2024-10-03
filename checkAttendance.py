import sys
import requests

args = sys.argv
botToken = args[1]
channelId = args[2]
messageGASURL = args[3]
membersGasURL = args[4]

def main():
  messageData = getMessageData(messageGASURL)
  messageId = messageData["messageId"]

  yes_users = getReactions(botToken, channelId, messageId, "⭕")
  no_users = getReactions(botToken, channelId, messageId, "❌")

  members = getMembers(membersGasURL)
  for member in members:
    if member["discordId"] in yes_users or member["discordId"] in no_users:
      member["attendance"] = True
    else:
      member["attendance"] = False
  
  sendRemindAttendance(botToken, channelId, members)

def getMessageData(messageGASURL):
  r = requests.get(messageGASURL)
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
    users.append(user["id"])
  return users

def getMembers(membersGasURL):
  r = requests.get(membersGasURL)
  return r.json()

def sendRemindAttendance(botToken, channelId, members):
  message = (
    "お疲れ様です！\n"
    "以下の方は今日の活動の参加可否を教えてください！\n"
    "\n"
  )
  
  membersMessage = []
  for member in members:
    if not member["attendance"]:
      membersMessage.append(f"{member['name']}(<@{member['discordId']}>)")
  message += "、".join(membersMessage)
        
  url = f"https://discord.com/api/v10/channels/{channelId}/messages"
  headers = {
    "Authorization": f"Bot {botToken}",
    "Content-Type": "application/json",
  }
  payload = {
    "content": message,
  }
  requests.post(url, headers=headers, json=payload)