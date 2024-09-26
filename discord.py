from asyncio import sleep
import sys
import datetime
import requests

def main():
    args = sys.argv
    botToken = args[1]
    channelId = args[2]

    messageId = askAttendance(botToken, channelId)
    createReaction(botToken, channelId, messageId, "⭕")
    createReaction(botToken, channelId, messageId, "❌")
    print("done")

def askAttendance(botToken, channelId):
    url = f"https://discord.com/api/v10/channels/{channelId}/messages"
    headers = {
        "Authorization": f"Bot {botToken}",
        "Content-Type": "application/json",
    }
    ruleId = 1288860377634963558
    payload = {
        "embeds": [
            {
                "title": f"{get_time()}の活動の参加可否",
                "description": (
                    f"<@&{ruleId}>\n"
                    "お疲れ様です！\n"
                    "明日の参加可否を教えてください！\n"
                    "\n"
                    "リアクションをお願いします！\n"
                    ),
                "color": 4371196,
            }
        ],
        "content": f"<@&{ruleId}> 明日のサークルの参加可否を教えてください！",
    }
    r = requests.post(url, headers=headers, json=payload)
    print(r.json())
    return r.json()["id"]

def createReaction(botToken, channelId, messageId, reaction):
    url = f"https://discord.com/api/v10/channels/{channelId}/messages/{messageId}/reactions/{reaction}/@me"
    headers = {
        "Authorization": f"Bot {botToken}",
        "Content-Type": "application/json",
    }
    requests.put(url, headers=headers)
    print("done")
    


def get_time():
    nextDay = datetime.datetime.now() + datetime.timedelta(days=1)

    return nextDay.strftime("%Y-%m-%d")

main()