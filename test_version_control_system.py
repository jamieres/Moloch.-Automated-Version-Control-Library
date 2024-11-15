import os
from version_control_system import VersionControlSystem

changelog_path = "changelog.txt"

def reset_changelog():
    if os.path.exists(changelog_path):
        os.remove(changelog_path)

def check_changelog_content():
    with open(changelog_path, "r") as file:
        return file.read()

def test_version_control_system():
    print("Iniciando pruebas del sistema de control de versiones...")

    reset_changelog()
    vcs = VersionControlSystem()
	
    major_version = vcs.create_version_identifier("major")
    print(f"Versión Major generada: {major_version}")

    minor_version = vcs.create_version_identifier("minor")
    print(f"Versión Minor generada: {minor_version}")

    patch_version = vcs.create_version_identifier("patch")
    print(f"Versión Patch generada: {patch_version}")

    changelog_content = check_changelog_content()
    print("\nContenido del Changelog:")
    print(changelog_content)

    assert "Version:" in changelog_content, "Error: Changelog no contiene las entradas esperadas."
    assert "Type: major" in changelog_content, "Error: Entrada de 'major' no encontrada en changelog."
    assert "Type: minor" in changelog_content, "Error: Entrada de 'minor' no encontrada en changelog."
    assert "Type: patch" in changelog_content, "Error: Entrada de 'patch' no encontrada en changelog."
    print("Pruebas completadas exitosamente.")

if __name__ == "__main__":
    test_version_control_system()
