from config import ConfigManager
from version_manager import VersionManager
from hashing import VersionHasher
from changelog_manager import ChangelogManager

class VersionControlSystem:


    def __init__(self):
        self.config_manager = ConfigManager()
        self.version_manager = VersionManager()
        self.changelog_manager = ChangelogManager(changelog_path="changelog.txt")
        self.hasher = None

    def create_version_identifier(self, change_type):
        name, version = self.version_manager.update_version(change_type)

        self.hasher = VersionHasher(name, version)
        hash_value = self.hasher.generate_sha256_hash()

        full_version_identifier = f"{name}_{version}_{hash_value}"

        self.changelog_manager.add_entry(name, version, hash_value, change_type)

        return full_version_identifier
