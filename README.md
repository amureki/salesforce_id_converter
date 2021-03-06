# Salesforce Id converter

[![PyPI](https://img.shields.io/pypi/v/salesforce_id_converter.svg)](https://pypi.org/project/salesforce_id_converter/)
[![GitHub license](https://img.shields.io/github/license/amureki/salesforce_id_converter.svg)](https://github.com/amureki/salesforce_id_converter/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/amureki/salesforce_id_converter.svg?branch=master)](https://travis-ci.org/amureki/salesforce_id_converter)

Simply converts 15 character id into a 18 character id.
Visit [Salesforce StackExchange](http://salesforce.stackexchange.com/questions/1653/what-are-salesforce-ids-composed-of) article for details.

## Usage:

```bash
pip install salesforce_id_converter
sfc 00558000001N0Ke
```

And you will get the next output:
```bash
You converted 15 character `00558000001N0Ke` into 18 character:
00558000001N0KeAAK
New id has been copied to your clipboard
```
