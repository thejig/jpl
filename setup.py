"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="jpl",
    version="0.0.1",
    description="Jiggy Playbook Linter",
    long_description=long_description,
    url="https://github.com/thejig/jpl",
    author="Mitchell Bregman, Leon Kozlowski",
    author_email="mitchbregs@gmail.com, leonkozlowski@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="yaml lint linter",
    packages=find_packages(),
    install_requires=["pytest", "pyyaml", "Click"],
    entry_points=
        """
    [console_scripts]
    jpl=jpl.cli.main_cli:lint
        """,
)
