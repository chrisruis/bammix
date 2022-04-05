from setuptools import setup, find_packages
from codecs import open
from os import path
import os
import re
import io

# Get version strip
def read(*names, **kwargs):
    with io.open(os.path.join(os.path.dirname(__file__), *names),
                 encoding=kwargs.get("encoding", "utf8")) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

#Import README
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='bammix',
      version=find_version("bammix/__init__.py"),
      author='Chris Ruis',
      author_email='cr628@cam.ac.uk',
      description='bammix',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/chrisruis/bammix',
      install_requires=[
            "pysam>=0.17.0",
            "matplotlib>=3.2.1"
        ],
      python_requires=">=3.6.0",
      packages=['bammix'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
        ],
      entry_points={
          'console_scripts': [
              'bammix = bammix.command:main',
            ],
          },
      )
