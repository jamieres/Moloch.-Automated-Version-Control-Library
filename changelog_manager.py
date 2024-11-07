import os
from config import ConfigManager

class ChangelogManager:
    def __init__(self, changelog_path="changelog.txt"):
        self.changelog_path = changelog_path
        self.config_manager = ConfigManager()

        if not os.path.exists(self.changelog_path):
            with open(self.changelog_path, "w") as file:
                file.write("Changelog Inicial\n\n")

    def add_entry(self, name, version, hash_value, change_type):
        visibility = self.config_manager.get_visibility_classification(change_type)

        entry = f"Version: {name}_{version}_{hash_value}\nType: {change_type}\nVisibility: {visibility}\n---\n"

        with open(self.changelog_path, "a") as changelog_file:
            changelog_file.write(entry)
