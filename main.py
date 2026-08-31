
#Rule based AI Python ChatBot

import datetime
import time

name= input("Welcome:) Enter your name: ")
presentHour= datetime.datetime.now().hour 

if 5 <= presentHour <= 12:
    print("Good morning, ", name)
elif 12 <= presentHour <= 16:
    print("Good afternoon, ", name)
elif 16 <= presentHour <= 22:
    print("Good evening, ", name)
else:
    print("Good night, "), name


print("NAMASTE!! Welcome to your ChatBOt")
print("You can ask me basic questions, if you want to exit from the bot type 'bye' anytime")

# Chatbot Memory Creation [ dictionary of responses]

responses = {
    "hello": "Hi, Welcome!! How can I help you",
    "how are you": "I am very fine. Thank You",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great:) I am also happy to hear that",
    "full form of html": "Hypertext markup language",
    "square of 5": "Square of 5 is 25"
}

# Method/Function to get response of ChatBot

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower().strip()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I'll learn that soon"


# Take user input

while True:
    userInput= input("Please ask your question: ")
    reply= getResponseOfBot(userInput)
    print("Bot Response :", reply)

    if "bye" in userInput.lower():
        break