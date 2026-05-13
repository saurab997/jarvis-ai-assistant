from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def aiResponse(command):
   client = OpenAI(
         api_key = os.getenv("OPENAI_API_KEY")
   )

   completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses and do not ask follow up questions."},
        {"role": "user", "content": command}
    ]
   )

   return completion.choices[0].message.content