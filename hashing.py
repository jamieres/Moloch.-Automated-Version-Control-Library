import hashlib

class VersionHasher:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def generate_sha256_hash(self):
        sha256 = hashlib.sha256()
        input_string = f"{self.name}_{self.version}"
        sha256.update(input_string.encode('utf-8'))
        return sha256.hexdigest()
