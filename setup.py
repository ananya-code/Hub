import os
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install

project = "hub"
VERSION = "0.12.6"

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md")) as f:
    long_description = f.read()

with open(os.path.join(this_directory, "requirements.txt"), "r") as f:
    requirements = f.readlines()

setup(
    name=project,
    version=VERSION,
    description="Snark Hub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Snark AI Inc.",
    author_email="support@activeloop.ai",
    url="https://github.com/snarkai/hub",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords="snark-hub",
    python_requires=">=3",
    install_requires=requirements,
    setup_requires=[],
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "hub = hub.cli.command:cli",
            "hub-local = hub.cli.local:cli",
            "hub-dev = hub.cli.dev:cli",
        ]
    },
    tests_require=["pytest", "mock>=1.0.1"],
)
