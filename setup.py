from os import path
from setuptools import setup, find_packages

root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='salesforce_id_converter',
    description='Convert 15 character Salesforce id into a 18 character id',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.2',
    author='Rustem Saiargaliev',
    author_email='r.sayargaliev@gmail.com',
    license='Apache-2',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/amureki/salesforce_id_converter.git',
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={
        'console_scripts': [
            'sfc=salesforce_id_converter.cli:main',
        ],
    },
    test_suite='tests',
)
