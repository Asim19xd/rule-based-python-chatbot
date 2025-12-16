# Rule based Ai Python Chatbot

import datetime
import time

name = input("Welcome,Please enter your name:") 
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
   print("Good Morning Hermano", name)

elif 11 <= presentHour <= 17:
   print("Good Afternoon", name)

elif 17 <= presentHour <= 19:
   print("Good Evening", name)
else: 
   print("Good Night", name)

print("Hello! Welcome to the Chatbot")
print("You can ask me basic questions, Type 'bye' to exit the chat")

# Chatbot Memory Creation
responses = { 
    "hello": "Hi, Welcome! How may i help you?",
    "how are you": "I am fine ! What about you?",
    "who are you": "I am a personal chatbot designed to have a conversation with you",
    "motivate me": "Keep going and improving whatever you do each bug in your project makes you stronger and better coder",
    "fine": "Great to hear that",
    "whats the use of python": "Python is used to overcome the traditional programming languages", 
}

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "i dont know about that"
while True:
    user_input = input("Please ask your question? ")
    reply = getResponseBot(user_input)
    print("Bot Response:", reply)

    if "bye" in user_input.lower():
        print("Haha, Have a great day", name)
        break
