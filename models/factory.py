import os
from langchain_openai import AzureChatOpenAI
from models.llm_settings import LLM_Settings

class Factory:
  
    def create(self, model_name):
        if model_name == 'gpt_azure_4o':
            azure_llm_settings = LLM_Settings().instance_model_settings(model_name)

            #Itś necessary for the lib
            os.environ["AZURE_OPENAI_VERSION"] = azure_llm_settings.api_version
            os.environ["AZURE_OPENAI_DEPLOYMENT"] = azure_llm_settings.deployment
            os.environ["AZURE_OPENAI_ENDPOINT"] = azure_llm_settings.endpoint
            os.environ["AZURE_OPENAI_KEY"] = azure_llm_settings.key


            model = AzureChatOpenAI(
                openai_api_version = azure_llm_settings.api_version,
                azure_deployment = azure_llm_settings.deployment,
                azure_endpoint = azure_llm_settings.endpoint,
                api_key = azure_llm_settings.key,
                openai_api_type = 'azure'
            )

            return model
