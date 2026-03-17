import os
from openai import OpenAI

client = OpenAI()

def simple_agent(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are a helpful FAQ assistant for a tourism company in Chennai."},
                  {"role":"user","content":user_input}]
    )
    return response.choices[0].message.content

print(simple_agent("list down 5 places to visit in Chennai on a same day?"))