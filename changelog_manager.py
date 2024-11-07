
import os
from config import ConfigManager

class ChangelogManager:
    """
    ChangelogManager gestiona la creación y almacenamiento de changelogs para registrar cada versión generada.
    Incluye la clasificación de visibilidad (público, confidencial, secreto) de cada cambio.
    """

    def __init__(self, changelog_path="changelog.txt"):
        self.changelog_path = changelog_path
        self.config_manager = ConfigManager()
        
        # Crear el archivo si no existe
        if not os.path.exists(self.changelog_path):
            with open(self.changelog_path, "w") as file:
                file.write("Changelog Inicial\n\n")

    def add_entry(self, name, version, hash_value, change_type):
        """
        Añade una entrada al changelog con nombre, versión, hash, y clasificación de visibilidad.
        :param name: Nombre temático de la versión.
        :param version: Número de versión en formato "vX.Y.Z".
        :param hash_value: Hash SHA256 de la versión.
        :param change_type: Tipo de cambio ("major", "minor", "patch").
        """
        # Determinar la clasificación de visibilidad del cambio
        visibility = self.config_manager.get_visibility_classification(change_type)

        # Crear la entrada del changelog
        entry = f"Version: {name}_{version}_{hash_value}\nType: {change_type}\nVisibility: {visibility}\n---\n"

        # Guardar la entrada en el archivo changelog
        with open(self.changelog_path, "a") as changelog_file:
            changelog_file.write(entry)
