from documentation import conf

from setuptools import setup

with open('requirements.rst', 'r') as fh_in:
    packages = fh_in.read().split()
    packages = [package.split('==')[0] for package in packages]

setup(
    name=conf.project,
    author=conf.author,
    version=conf.release,
    py_modules=['similitude'],
    install_requires=packages,
    entry_points='''
        [console_scripts]
        similitude=similitude:similitude
    ''',
)
