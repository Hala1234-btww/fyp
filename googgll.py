import pyttsx3
engine = pyttsx3.init()
#from googletrans import Translator
#import googletrans

#print(googletrans.LANGUAGES)
#tr = Translator()
#a = tr.translate("Hello Hi I am halla", src= 'en', dest='ur')
#print(a.text)

hi=' آپ کسی ہے '
hi2="Welcome to pakistan hope son you are enjoying"
# getting details of current speaking rate
rate = engine.getProperty('rate')
# printing current voice rate
print (rate)
# setting up new voice rate
engine.setProperty('rate', 139)

"""VOLUME"""
#getting to know current volume level (min=0 and max=1)
volume = engine.getProperty('volume')
#printing current volume level
print (volume)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')
print(voices)
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


engine.say(hi)
engine.runAndWait()
engine.stop()
engine.say(hi2)
engine.runAndWait()
engine.stop()

engine.runAndWait()