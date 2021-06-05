from setuptools import find_packages
from setuptools import setup

setup(
    name="qutelaunch",
    description="A startpage for Qutebrowser designed to be left quickly.",
    url="https://github.com/Kharacternyk/qutelaunch",
    version="0.0.0",
    license="GPLv3",
    author="Nazar Vinnichuk",
    keywords="qutebrowser startpage",
    packages=find_packages(),
    package_data={"qutelaunch": ["templates/*"]},
    install_requires=["flask", "dataclasses; python_version < '3.7'"],
)
