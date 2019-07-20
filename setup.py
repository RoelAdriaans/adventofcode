from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="adventofcode2018",
    author="Roel Adriaans",
    author_email="roel@adriaans.org",
    url="https://github.com/roeladriaans",
    # version="0.0.2",
    entry_points={"console_scripts": ["adventofcode = main:main"]},
    packages=find_packages(where="src", exclude=["tests.*", "test*"]),
    package_dir={"": "src"},
    install_requires=requirements,
    include_package_data=True,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
