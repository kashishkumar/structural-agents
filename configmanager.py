from yaml import safe_load
    
class ConfigManager:
    def __init__(self, path):
        self.config = self.load_config(path)

    def load_config(self, path):
        with open(path) as f:
            return safe_load(f)

    def get_config(self):
        return self.config
    

config = ConfigManager("config.yaml")