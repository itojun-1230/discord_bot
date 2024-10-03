import sys
import checkAttendance
import sendAskAttendance

args = sys.argv
eventType = args[1]
botToken = args[2]
channelId = args[3]
messageGASURL = args[4]
membersGasURL = args[5]

def main():
  if(eventType == "send"):
    sendAskAttendance.main(botToken, channelId, messageGASURL)
  elif(eventType == "check"):
    checkAttendance.main(botToken, channelId, messageGASURL, membersGasURL)

main()