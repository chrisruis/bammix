from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import glob
import os
import pkg_resources

from bammix import __version__, _program

setup(name='bammix',
      version=__version__,
      packages=find_packages(),
      scripts=["bammix/scripts/bammix_functions.py"],
      install_requires=[
            "pysam>=0.17.0",
            "matplotlib>=3.2.1"
        ],
      description='bammix',
      url='https://github.com/chrisruis/bammix',
      author='Chris Ruis',
      author_email='cr628@cam.ac.uk',
      entry_points="""
      [console_scripts]
      {program} = bammix.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)