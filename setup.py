from os.path import dirname, join
from pathlib import Path

from setuptools import setup, find_packages

def read(fname):
    """Read content of a file and return as a string."""
    return Path(join(dirname(__file__), fname)).read_text()


def get_requirements():
    """Return requirements with loose version restrictions."""
    return read("requirements.txt").replace("==", ">=").split("\n")

setup(
    name="pulumi_toolkit",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements(),
    author="Jeffrey Boisvert",
    author_email="info.jeffreyboisvert@gmail.com",
    description="A collection of reusable components and utils for pulumi programs in Python.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jdboisvert/python-pulumi-toolkit",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
