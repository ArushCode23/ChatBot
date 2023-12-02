import pyttsx3
import openai

engine = pyttsx3.init()

engine.say("Hello how can i help you i am your personal AI Assistant Mino")
engine.runAndWait()

name = input("What is your name: ")

engine.say(f"Hello, {name} how can i help you today")
engine.runAndWait()
openai.api_key = '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'

while True:
 prompt = input("You: ")

 response = openai.Completion.create(
    engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150
 )

 print("Bot: ",response.choices[0].text.strip(),engine.say(response.choices[0].text.strip()))
 engine.runAndWait()
