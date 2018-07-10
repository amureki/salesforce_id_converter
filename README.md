# Salesforce Id converter

[![Build Status](https://travis-ci.org/amureki/salesforce_id_converter.svg?branch=master)](https://travis-ci.org/amureki/salesforce_id_converter)

Simply converts 15 character id into a 18 character id.
Check out http://salesforce.stackexchange.com/questions/1653/what-are-salesforce-ids-composed-of for details.

## Usage:

```bash
pip install sfc
sfc 00558000001N0Ke
```

And you will get the next output:
```bash
You converted 15 character `00558000001N0Ke` into 18 character:
00558000001N0KeAAK
New id has been copied to your clipboard
```
