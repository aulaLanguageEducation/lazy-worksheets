from setuptools import setup, find_packages
import os

setup(
    name='lazy-worksheets',
    version='0.1.0',
    author='aulaLanguageEducation',
    packages=find_packages(),
    url='https://github.com/aulaLanguageEducation/lazy-worksheets',
    license='LICENSE',
    description='Used to turn boring websites into lazy worksheets!',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read(),
)

# import spacy language model
os.system('cmd /k "python -m spacy download en_core_web_sm"')

