from setuptools import setup
from setuptools import find_packages


def requirements(path):
    with open(path) as req:
        return [x.strip() for x in req.readlines() if not x.startswith('-')]


setup(
    author='amancevice',
    author_email='smallweirdnumber@gmail.com',
    description='Parse financial strings to numbers.',
    install_requires=requirements('requirements.txt'),
    name='finparse',
    packages=find_packages(exclude=['tests']),
    setup_requires=['setuptools_scm'],
    tests_require=requirements('requirements-dev.txt'),
    url="http://github.com/amancevice/finparse",
    use_scm_version=True,
)
