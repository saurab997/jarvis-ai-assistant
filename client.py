from openai import OpenAI
import os
client = OpenAI()

response = client.responses.create(
    api_key = os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)