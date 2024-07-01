import pyttsx3
import datetime
import random

currentTime = datetime.datetime.now()
Time = "W"
motivation = ['Take it easy','Tough times do not last','Stay Strong','Have Faith','Just keep going']
length = len(motivation)
random_value = random.randint(0,length-1)
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


if currentTime.hour < 12:
    Time = "M"
elif currentTime.hour <18:
    Time = "A"
elif currentTime.hour<22:
    Time = "E"
else:
    Time = "Welcome"

converter = pyttsx3.init()  #Initializes the converter
converter.setProperty('rate',130)
converter.setProperty('volume',0.9)

match Time:
    case "M": converter.say('Good Morning')
    case "A": converter.say('Good Afternoon')
    case "E":converter.say('Good Evening')        
    case _:converter.say('Welcome')  

converter.runAndWait()
converter.setProperty('voice',voice_id)
converter.say(motivation[random_value])

converter.runAndWait()