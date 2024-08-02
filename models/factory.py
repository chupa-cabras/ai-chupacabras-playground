import os
import google.generativeai as genai

from chromadb import Embeddings
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from models.llm_settings import LLM_Settings

class Factory:
  
    def create(self, model_name):
        load_dotenv()

        if model_name == 'gpt_azure_4o':
            azure_llm_settings = LLM_Settings().instance_model_settings(model_name)

            #It's necessary for the lib
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
        if model_name == 'openai_text_embedding_3_small':
            llm_settings = LLM_Settings().instance_model_settings(model_name)
            return OpenAIEmbeddings(openai_api_key = llm_settings.key, model = 'text-embedding-3-small')

        return None