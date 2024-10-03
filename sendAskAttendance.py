import datetime
import sys
import time
import requests

args = sys.argv
botToken = args[1]
channelId = args[2]
membersGasURL = args[3]

def main():

    messageResult = askAttendance(botToken, channelId)
    messageId = messageResult[0]
    title = messageResult[1]
    createReaction(botToken, channelId, messageId, "⭕")
    createReaction(botToken, channelId, messageId, "❌")

    postMessageId(messageId, title, messageGASURL)

def askAttendance(botToken, channelId):
    url = f"https://discord.com/api/v10/channels/{channelId}/messages"
    headers = {
        "Authorization": f"Bot {botToken}",
        "Content-Type": "application/json",
    }
    roleId = 1288860377634963558
    title = f"{get_time()}の活動の参加可否"
    payload = {
        "embeds": [
            {
                "title": title,
                "description": (
                    f"<@&{roleId}>\n"
                    "お疲れ様です！\n"
                    "明日の参加可否を教えてください！\n"
                    "\n"
                    "リアクションをお願いします！\n"
                    ),
                "color": 4371196,
            }
        ],
        "content": f"<@&{roleId}> 明日のサークルの参加可否を教えてください！",
    }
    r = requests.post(url, headers=headers, json=payload)
    print(r.json())
    return r.json()["id"], r.json()["embeds"][0]["title"]

def createReaction(botToken, channelId, messageId, reaction):
    url = f"https://discord.com/api/v10/channels/{channelId}/messages/{messageId}/reactions/{reaction}/@me"
    headers = {
        "Authorization": f"Bot {botToken}",
        "Content-Type": "application/json",
    }
    requests.put(url, headers=headers)
    time.sleep(1)

def postMessageId(messageId, title, messageGASURL):
    requests.post(messageGASURL, json={"messageId": messageId, "title": title})

def get_time():
    nextDay = datetime.datetime.now() + datetime.timedelta(days=1)

    return nextDay.strftime("%Y-%m-%d")