from setuptools import setup
from setuptools import find_packages

setup(
    author='amancevice',
    author_email='smallweirdnumber@gmail.com',
    description='Parse financial strings to numbers.',
    name='finparse',
    packages=find_packages(exclude=['tests']),
    setup_requires=['setuptools_scm'],
    url="http://github.com/amancevice/finparse",
    use_scm_version=True,
)
