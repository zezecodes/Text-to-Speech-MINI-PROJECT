from gtts import gTTS 
import os

print("Welcome to the Text-to-Speech Converter")

userNameInput = input("Please tell us your name: ")
print(f"Hello, {userNameInput}")

textToBeConverted = input("Kindly input the text you want to be converted here: ")

speech = gTTS(text=textToBeConverted, lang='en', slow=False)
speech.save("speech.mp3")
os.system("speech.mp3")

print(textToBeConverted)