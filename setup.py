#!/usr/bin/env python
from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='PySyncThru',
      version='0.3.0.1',
      description='Automated JSON API based communication with Samsung SyncThru Web Service',
      author='Niels Mündler',
      author_email='n.muendler@web.de',
      url='https://github.com/nielstron/pysyncthru/',
      py_modules=['pysyncthru'],
      packages=find_packages(),
      install_requires=[
          'demjson',
          'requests',
      ],
      long_description=long_description,
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Object Brokering',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='python syncthru json api samsung printer',
      python_requires='>=3',
      )
