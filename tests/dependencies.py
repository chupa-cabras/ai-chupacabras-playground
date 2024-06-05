from models.factory import Factory
from langchain_core.messages import HumanMessage

model = Factory().create('gpt_azure_4o')

message = HumanMessage(
    content="Qual o animal que come com o rabo ?"
)
response = model.invoke([message])
print(response)
