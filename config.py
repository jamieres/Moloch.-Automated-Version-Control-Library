import json
import os

class ConfigManager:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            default_config = {
                "versioning": {
                    "major_criteria": ["API change", "New Feature"],
                    "minor_criteria": ["Enhancement", "Fix"],
                    "names_theme": "demons",
                    "visibility": {
                        "public": ["Enhancement"],
                        "confidential": ["API change", "Fix"],
                        "secret": ["New Feature"]
                    }
                }
            }
            with open(self.config_path, 'w') as config_file:
                json.dump(default_config, config_file, indent=4)
            return default_config
        else:
            with open(self.config_path, 'r') as config_file:
                return json.load(config_file)

    def get_versioning_criteria(self, change_type):
        if change_type in self.config["versioning"]["major_criteria"]:
            return "major"
        elif change_type in self.config["versioning"]["minor_criteria"]:
            return "minor"
        return None

    def get_visibility_classification(self, change_type):
        for visibility, types in self.config["versioning"]["visibility"].items():
            if change_type in types:
                return visibility
        return "public"

    def get_names_theme(self):
        return self.config["versioning"].get("names_theme", "demons")

config_manager = ConfigManager()
config_loaded = {
    "Major Criteria for Changes": config_manager.get_versioning_criteria("API change"),
    "Visibility Classification for New Feature": config_manager.get_visibility_classification("New Feature"),
    "Theme for Version Names": config_manager.get_names_theme()
}

config_loaded
