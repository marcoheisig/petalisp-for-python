"""The petalisp setup.

See:
https://github.com/marcoheisig/petalisp-for-python
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='petalisp',
    version='0.1.0',
    description='A powerful array programming library.',
    long_description=readme(),
    long_description_content_type='text/x-rst',
    license='MIT',
    url='https://github.com/marcoheisig/petalisp-for-python',
    author='Marco Heisig',
    author_email='marco.heisig@fau.de',
    install_requires=['numpy', 'cl4py'],
    extras_require={},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Lisp' ,
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
    include_package_data = True,
)
