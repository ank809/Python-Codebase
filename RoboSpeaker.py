import pyttsx3

print("Welcome to Robo speaker. Created by Ankita")

engine = pyttsx3.init()

while True:
    x = input('Enter the text you want to say: ')
    if x == 'q':
        break
    engine.say(x)
    engine.runAndWait()
