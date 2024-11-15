# Moloch: Automated Version Control Library

This library allows you to manage the version control of a project in an automated way using thematic names, semantic version numbers and SHA256 hashes to identify each version in a unique and precise way.


## Library Usage

1. Initialize the version control system:
```
from version_control_system import VersionControlSystem
vcs = VersionControlSystem()
```

2. Generate a version identifier based on the change type:
```
version_major = vcs.create_version_identifier("major")
version_minor = vcs.create_version_identifier("minor")
version_patch = vcs.create_version_identifier("patch")
```

## Implementation
1. Manually copy the library source files (e.g. version_control_system.py, config.py, etc.) to the project root directory or a subfolder. 
```
moloch_versioning/
├── __init__.py
├── config.py
├── hashing.py
├── name_generator.py
├── version_manager.py
├── changelog_manager.py
└── version_control_system.py
```
	### Usage:
	Import modules directly from the copied folder.
	```
	python
	from version_control_system import VersionControlSystem
	```
	
2. Install as a Local Package with pip ("src" folder).
```
pip install path/to/moloch_versioning-0.1-py3-none-any.whl
```
	### Usage:
	Once installed, you can import the library like any installed package.
	```
	python
	from moloch_versioning import VersionControlSystem
	```

3. Install from PyPI (Remote). * https://pypi.org/project/moloch-versioning/0.1/
```
pip install moloch_versioning
```
	### Usage:
	As in the local case, the package is imported like any installed library.
	```
	python
	from moloch_versioning import VersionControlSystem
	```

## Recommendation
* Small Projects or Tests:* Copy files directly.
* Clean Management Across Multiple Projects:* Install as a local package or from PyPI.
* Team Collaboration:* Use as a submodule or from PyPI.


## License

This library is distributed under the **GNU General Public License v3.0 (GPL-3.0)**. Check LICENSE file for more details.

# Note
This is a pre-release version, so if you encounter any issues please let me know: jamieres-at-gmail-dot-com
