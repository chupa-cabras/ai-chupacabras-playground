import os
import time

import google.generativeai as genai
from models.llm_settings import LLM_Settings

llm_settings = LLM_Settings().instance_model_settings('gemini_15pro')
genai.configure(api_key=llm_settings.key)

def upload_to_gemini(path, mime_type=None):
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

def wait_for_files_active(files):
  print("Waiting for file processing...")
  for name in (file.name for file in files):
    file = genai.get_file(name)
    while file.state.name == "PROCESSING":
      print(".", end="", flush=True)
      time.sleep(10)
      file = genai.get_file(name)
    if file.state.name != "ACTIVE":
      raise Exception(f"File {file.name} failed to process")
  print("...all files ready")
  print()

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain"
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config
)

files = [
  upload_to_gemini("tmp/environment_analyzer_example.mp4", mime_type="video/mp4"),
]

wait_for_files_active(files)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        files[0],
      ],
    }
  ]
)

response = chat_session.send_message("Gostaria que descrevesse o vídeo com a maior riqueza de detalhes possível. Caso encontre livros, revistas, fotos, etc , me descreve o conteúdo, título, estado físico . Obrigado .")

print(response.text)