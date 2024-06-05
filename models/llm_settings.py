from envyaml import EnvYAML
import os
from box import Box


class LLM_Settings:
    def __init__(self):
        
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        settings_file = os.path.join(root_path, 'settings.yml')

        if not os.path.isfile(settings_file):
            raise FileNotFoundError(f"Settings file '{settings_file}' not found.")
             
        self.content = EnvYAML(settings_file)['models']

    def instance_model_settings(self, model_name):
        return Box(self.content[model_name])

