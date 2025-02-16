from setuptools import setup, find_packages

setup(
    name="sessio",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="uvoob",
    description="A lightweight session management library for Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/uvoob/sessio",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)