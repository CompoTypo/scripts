import sys
import pyttsx3  # Used espeak to synthesize speech with mbrola to improve voice quality


def getFileText(path):
    file = open(path, 'rt')
    return file.readlines()


def constructSpeechEngine():
    engine = pyttsx3.init()  # object creation""" RATE"""
    rate = engine.getProperty(
        'rate')   # getting details of current speaking rate
    print(rate)  # printing current voice rate

    engine.setProperty('rate', 125)     # setting up new voice rate

    """VOLUME"""
    # getting to know current volume level (min=0 and max=1)
    volume = engine.getProperty('volume')
    print(volume)  # printing current volume level

    # setting up volume level  between 0 and 1"""VOICE"""
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')  # getting details of current voice

    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    # changing index, changes voices. 1 for femaleengine.say("Hello World!")
    engine.setProperty('voice', voices[2].id)
    return engine


text_lines = getFileText(sys.argv[1])

engine = constructSpeechEngine()
print(engine.getProperty('voice'))

for text_line in text_lines:
    engine.say(text_line)
engine.runAndWait()
engine.stop()
