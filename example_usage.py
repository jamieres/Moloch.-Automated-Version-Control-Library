
# Ejemplo de uso de la librería de control de versiones automatizado

from version_control_system import VersionControlSystem

# Inicialización del sistema de control de versiones
vcs = VersionControlSystem()

# Generación de identificadores de versión según el tipo de cambio realizado en el proyecto
version_major = vcs.create_version_identifier("major")
version_minor = vcs.create_version_identifier("minor")
version_patch = vcs.create_version_identifier("patch")

# Imprimir los identificadores generados
print("Identificador de versión (Cambio Mayor):", version_major)
print("Identificador de versión (Cambio Menor):", version_minor)
print("Identificador de versión (Cambio Patch):", version_patch)
