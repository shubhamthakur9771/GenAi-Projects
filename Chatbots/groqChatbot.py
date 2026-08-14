import os
from groq import Groq
from dotenv import load_dotenv
 
# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
 
# Create client
client = Groq(api_key=api_key)
 
print("Groq Chat App (type 'exit' to quit)\n")
 
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]
 
while True:
    user_input = input("You: ")
 
    if user_input.lower() == "exit":
        break
 
    # Add user message
    messages.append({"role": "user", "content": user_input})
 
    # Call Groq API
    response = client.chat.completions.create(
        #model="llama3-8b-8192",   # fast & good model
        model="llama-3.3-70b-versatile",
        messages=messages
    )
 
    reply = response.choices[0].message.content
 
    # Print response
    print("Bot:", reply, "\n")
 
    # Save conversation
    messages.append({"role": "assistant", "content": reply})