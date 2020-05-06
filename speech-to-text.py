import speech_recognition as sr     # import the library
import pyperclip as clip

r = sr.Recognizer()                 # initialize recognizer
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    r.adjust_for_ambient_noise(source)  # here
    print("Speak Anything :")
    audio = r.listen(source)        # listen to the source
    try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly

    try:
        clip.copy("{}".format(text))
    except:
        print("Clipboard copy didnt work")