from version_control_system import VersionControlSystem

vcs = VersionControlSystem()

version_major = vcs.create_version_identifier("major")
version_minor = vcs.create_version_identifier("minor")
version_patch = vcs.create_version_identifier("patch")

print("Identificador de versión (Cambio Mayor):", version_major)
print("Identificador de versión (Cambio Menor):", version_minor)
print("Identificador de versión (Cambio Patch):", version_patch)
