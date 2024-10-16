#
# small tool that calls Azure OpenAI with a simple task
#
import os
from openai import AzureOpenAI
    
client = AzureOpenAI(
#    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
#    api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
#    api_version = os.getenv("OPENAI_API_VERSION")
)
    
print('Sending a test completion job')
response = client.chat.completions.create(
  model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
  temperature=1.5,
  messages=[
    {"role": "system", "content": "You are a Marketeer. You create very creative slogans and texts for your clients."},
    {"role": "user", "content": "Please write a tagline for an ice cream shop."}
  ],
)

print(response.choices[0].message.content)
