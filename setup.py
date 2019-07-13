from setuptools import setup, find_packages

setup(
    name="adventofcode2018",
    author="Roel Adriaans",
    author_email="roel@adriaans.org",
    url="https://github.com/roeladriaans",
    version="0.0.1",
    entry_points={"console_scripts": ["adventofcode = main:main"]},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["Click"],
)
