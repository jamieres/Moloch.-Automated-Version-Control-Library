import random

class NameGenerator:
    def __init__(self, theme="demons"):
        self.theme = theme
        self.names = self._load_names()

    def _load_names(self):
        demon_names = [
            "moloch", "baal", "asmodeus", "belial", "lucifer", "beelzebub", 
            "mammon", "azazel", "aamon", "dagon", "baphomet", "abaddon"
        ]
        return demon_names

    def generate_name(self):
        return random.choice(self.names)

name_generator = NameGenerator()
generated_name = name_generator.generate_name()

generated_name
