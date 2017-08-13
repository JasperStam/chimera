#! /usr/bin/env python3
import os
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='chimera',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A framework for websocket APIs.',
    author='Jasper Stam',
    author_email='jasper@strnk.nl',
    url='https://github.com/JasperStam/chimera',
    classifiers=[],
    install_requires=[
        'gevent >= 1.1.2',
        'greenlet >= 0.4.12',
        'Flask >= 0.12.0',
        'Flask-Script >= 2.0.5',
        'Flask-Sockets >= 0.2.1',
        'Flask-SQLAlchemy >= 2.1',
        'Flask-Migrate >= 2.0.3',
        'pyjwt >= 1.4.2',
        'python-dateutil >= 2.6.0',
        'python-dotenv >= 0.6.3',
        'requests >= 2.13.0',
    ],
    test_suite='tests'
)