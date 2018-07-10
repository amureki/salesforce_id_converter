from setuptools import setup, find_packages

setup(
    name='salesforce_id_converter',
    version='0.1.1',
    description='Convert 15 character Salesforce id into a 18 character id',
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
