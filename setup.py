import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

with open(os.path.join('.', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ml_training_queue',
    version='0.0.5',
    author='deeepwin',
    author_email='deeepwin@gmail.com',
    url='',
    description='Machine learning queue to send jpbs to.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mlq-pusher = ml_training_queue.pusher:pusher',
            'mlq-executor = ml_training_queue.executor:executor'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords='ml_training_queue manage-tasks queue tasks python package',
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True
)
