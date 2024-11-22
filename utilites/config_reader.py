import yaml
import os


class ConfigReader:
    CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), "../utilites/config_file.yml")

    def __init__(self):
        self.config = self._load_config()

    def _load_config(self):
        with open(self.CONFIG_FILE_PATH, "r") as f:
            return yaml.safe_load(f)["config"]

    def return_value(self, key):
        return self.config.get(key)
