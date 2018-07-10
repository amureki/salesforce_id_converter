from setuptools import setup, find_packages

required_packages = [
    'requests',
]

setup(
    name='salesforce_id_converter',
    version='0.0.1',
    description='Convert 15 character Salesforce id into a 18 character id',
    author='Rustem Saiargaliev',
    author_email='r.sayargaliev@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/amureki/salesforce_id_converter.git',
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={
        'console_scripts': [
            'sfc = salesforce_id_converter.cli:main',
        ],
    },
    install_requires=required_packages,
    test_suite='tests',
)