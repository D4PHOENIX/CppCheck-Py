# setup.py
from setuptools import setup, find_packages

setup(
    name="CppCheck-Py",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi", "uvicorn", "pydantic", "pytest", "flake8"
    ],
)
