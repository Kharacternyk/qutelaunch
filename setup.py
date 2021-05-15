from setuptools import find_packages
from setuptools import setup

setup(
    name="qutelaunch",
    version="0.0.0",
    license="GPLv3+",
    install_requires=["jinja2"],
    tests_require=["pytest", "hypothesis"],
    url="https://github.com/Kharacternyk/qutelaunch",
    packages=find_packages(),
    package_data={"qutelaunch": ["templates/*"]},
)
