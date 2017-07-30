import os
from setuptools import setup

setup(
    name = "robloxlib",
    version = "7.0.0",
    install_requires=[
        "requests",
        "bs4",
        "lxml",
        "datefinder",
    ],
    author = "Noah Cristino",
    author_email = 'noahcristino@gmail.com',
    description = ("A simple library for getting info from ROBLOX's APIs."),
    license = "MIT",
    keywords = "roblox robloxapi requests",
    packages=['robloxlib'],
    download_url = "https://github.com/NoahCristino/robloxlib/archive/7.0.tar.gz",
    url = "https://github.com/NoahCristino/robloxlib",
    long_description= (""),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ],
)
