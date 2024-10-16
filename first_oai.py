#
# small tool that calls OpenAI with a simple task
#
import os
from openai import OpenAI
    
client = OpenAI()
    
print('Sending a test completion job')
response = client.chat.completions.create(
  model=os.getenv("OPENAI_MODEL"),
  temperature=1.5,
  messages=[
    {"role": "system", "content": "You are a Marketeer. You create very creative slogans and texts for your clients."},
    {"role": "user", "content": "Please write a tagline for an ice cream shop."}
  ],
)

print(response.choices[0].message.content)
