from setuptools import setup, find_packages

setup(
    name='example',
    description='description',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'Django',
    ],
    entry_points={
        'console_scripts': [
            'cliscript=example.commands:cli'
        ]
    },
    python_requires='>=3.7'
)
