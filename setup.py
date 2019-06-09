from setuptools import setup

setup(
    name="advent Of Code 2018",
    version="0.0.1",
    packages=["src"],
    entry_points={"console_scripts": ["adventofcode = src.__main__:main"]},
)
