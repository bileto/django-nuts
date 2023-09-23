#!/usr/bin/env python

import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

setup(
    name='django-nuts',
    version='2.0.0',
    description='Django application providing database of European NUTS and LAU',
    long_description=long_description,
    author='Bileto',
    author_email='support@bileto.com',
    license='BSD',
    url='https://github.com/bileto/django-nuts',
    packages=find_packages(),
    install_requires=[
        'django-admin',
        'lxml',
        'pyexcel-xls',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
    ],
)
