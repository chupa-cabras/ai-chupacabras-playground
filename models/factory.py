import os
from langchain_openai import AzureChatOpenAI
from models.llm_settings import LLM_Settings

class Factory:
  
    def create(self, model_name):
        if model_name == 'gpt_azure_4o':
            azure_llm_settings = LLM_Settings().instance_model_settings(model_name)

            os.environ["AZURE_OPENAI_API_KEY"] = azure_llm_settings.key
            os.environ["AZURE_OPENAI_ENDPOINT"] = azure_llm_settings.endpoint
            os.environ["AZURE_OPENAI_API_VERSION"] = azure_llm_settings.api_version
            os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = azure_llm_settings.deployment

            model = AzureChatOpenAI(
                openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
                azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"], 
            )

            return model
