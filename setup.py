from setuptools import setup, find_packages

setup(
    name="Advent Of Code 2018",
    version="0.0.1",
    entry_points={"console_scripts": ["adventofcode = main:main"]},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["Click"],
)
