from setuptools import find_packages
from setuptools import setup
from setuptools import find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    author='amancevice',
    author_email='smallweirdnumber@gmail.com',
    description='Parse financial strings to numbers',
    name='finparse',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests']),
    python_requires='>= 3.5',
    setup_requires=['setuptools_scm'],
    tests_require=[
        'flake8',
        'pytest',
        'pytest-cov',
    ],
    url='http://github.com/amancevice/finparse',
    use_scm_version=True,
)
