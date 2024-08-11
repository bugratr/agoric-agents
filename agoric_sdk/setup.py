from setuptools import setup, find_packages

setup(
    name="agoric_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Buğra Ayan",
    description="A Python implementation of the Agoric SDK",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/bugratr/agoric_sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
