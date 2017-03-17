import os
import re
from setuptools import setup


def version():
    search = r"^__version__ *= *['\"]([0-9.]+)['\"]"
    initpy = open("./finparse/__init__.py").read()
    return re.search(search, initpy, re.MULTILINE).group(1)


setup(
    name='finparse',
    version=version(),
    author='amancevice',
    author_email='smallweirdnumber@gmail.com',
    packages=['finparse'],
    url="http://www.smallweirdnumber.com",
    description='Parse financial strings to numbers.',
    long_description='''See GitHub_ for documentation.
.. _GitHub: https://github.com/amancevice/finparse''',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python"])
