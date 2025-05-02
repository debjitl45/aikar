# setup.py

from setuptools import setup, find_packages

setup(
    name='aikar',
    version='0.1.0',
    description='Simplifying Indian Taxes with Python',
    author='Debjit Karmakar',
    author_email='karmadebjit@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/debjitl45/aikar',
    packages=find_packages(),
    install_requires=[],
    keywords=['tax', 'india', 'income tax', 'capital gains', 'python'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)
