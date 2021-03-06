
from distutils.core import setup

with open('README.txt') as f:
    readme = f.read()

setup(
    name='vari',
    version='0.0.2',
    author='Phil Adams',
    author_email='phil@philadams.net',
    url='https://github.com/philadams/vari',
    license='LICENSE.txt',
    description='Python color representation conversions',
    long_description=readme,
    packages=['vari'],
    scripts=['bin/vari'],
)

