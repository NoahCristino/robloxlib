import os
from setuptools import setup

setup(
    name = "robloxlib",
    version = "0.0.1",
    install_requires=[
        "requests",
    ],
    author = "Noah Cristino",
    description = ("A simple library for getting info from ROBLOX's APIs."),
    license = "MIT",
    keywords = "roblox robloxapi requests",
    packages=['robloxlib'],
    url = "https://github.com/NoahCristino/robloxlib",
    long_description= (""),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License"
    ],
)
