from setuptools import setup

description = "Core libraries for natural language processing",

# To keep the docs pretty, use pandoc to "compile" the rst version of the README file
# before uploading to cheeseshop:
#
#     pandoc README.md -o README.rst
try:
    long_description = open('README.rst', 'r').read()
except:  # (IOError, ImportError, OSError, RuntimeError):
    long_description = description
    print('WARNING: Unable to find or read README.rst.')

setup(name="nlup",
      include_package_data=True,
      version="0.5",
      description=description,
      author="Kyle Gorman",
      author_email="gormanky@ohsu.edu",
      # url="http://github.com/cslu-nlp/nlup/",
      install_requires=["jsonpickle >= 0.9.0"],
      packages=["nlup"],
      )
