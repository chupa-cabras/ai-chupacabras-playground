import os
from openai import AzureOpenAI
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

print(os.getenv("AZURE_OPENAI_KEY"))
print(os.getenv("AZURE_OPENAI_VERSION"))
print(os.getenv("AZURE_OPENAI_ENDPOINT"))
print(os.getenv("AZURE_OPENAI_DEPLOYMENT"))



client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
)
    
deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT") #This will correspond to the custom name you chose for your deployment when you deployed a model. Use a gpt-35-turbo-instruct deployment. 
    
# Send a completion call to generate an answer
# print('Sending a test completion job')
# start_phrase = 'Write a tagline for an ice cream shop. '
# response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=10)
# print(start_phrase+response.choices[0].text)





  
completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "Who is DRI?",
        },
        {
            "role": "assistant",
            "content": "DRI stands for Directly Responsible Individual of a service. Which service are you asking about?"
        },
        {
            "role": "user",
            "content": "Opinion mining service"
        }
    ],
    extra_body={
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": "",
                    "index_name": "",
                    "authentication": {
                        "type": "system_assigned_managed_identity"
                    }
                }
            }
        ]
    }
)
      
print(completion.to_json())