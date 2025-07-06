# setup.py
from pathlib import Path

from setuptools import find_packages, setup

root = Path(__file__).parent.resolve()
long_description = (root / "README.md").read_text(encoding="utf-8")

setup(
    name="cppcheck-py",
    version="0.1.0",
    description="A lightweight C++ syntax checker in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daud Noman, Muhammad Arham Shafaat, Wassam Kham",
    python_requires=">=3.8",
    packages=find_packages(include=["backend", "backend.*"]),
    package_dir={"backend": "backend"},
    py_modules=["main"],
    install_requires=[
        "streamlit",
    ],
    entry_points={
        "console_scripts": [
            "cppcheck-py=backend.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License" "Operating System: OS Independent",
    ],
)
