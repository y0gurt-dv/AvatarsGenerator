from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Random avatars generator'


# Setting up
setup(
    name="AvatarsGenerator",
    version=VERSION,
    author="y0gurt-dv",
    author_email="<sigirt3@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['wand'],
    keywords=['python', 'avatars', 'random', 'random avatars', 'generator', 'avatars generator'],
    url='https://github.com/y0gurt-dv/AvatarsGenerator',
    classifiers=[
    ]
)