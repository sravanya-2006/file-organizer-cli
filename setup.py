from setuptools import setup, find_packages

setup(
    name='file-organizer-cli',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fileorganizer=file_organizer.cli:main',
        ],
    },
    install_requires=[],
    author='Sravanya',
    description='A CLI tool to organize files by extension',
    python_requires='>=3.6',
)
