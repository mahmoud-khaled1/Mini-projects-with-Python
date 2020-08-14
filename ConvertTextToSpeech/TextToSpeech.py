from gtts import gTTS
import os

f=open('D:\\Mini projects with Python\\ConvertTextToSpeech\\asd.txt','r')
txt=f.read()

language='en'
audio=gTTS(text=txt,lang=language,slow=False)
audio.save('mahh.mp3')
os.system('mahh.mp3')