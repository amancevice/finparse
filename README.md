# finparse

[![build](https://travis-ci.org/amancevice/finparse.svg?branch=master)](https://travis-ci.org/amancevice/finparse)
[![codecov](https://codecov.io/gh/amancevice/finparse/branch/master/graph/badge.svg)](https://codecov.io/gh/amancevice/finparse)
[![pypi](https://badge.fury.io/py/finparse.svg)](https://badge.fury.io/py/finparse)
[![python](https://img.shields.io/badge/python-2.7--3.5-blue.svg)](https://img.shields.io/badge/python-2.7--3.5-blue.svg)

Parse financial strings to number objects


## Installation

```bash
pip install finparse
```


## Usage

```python
import finparse

finparse.parse("$1,234,567.89")
# => 1234567.89

finparse.parse("€1.234.567,89", decimal=",")
# => 1234567.89

finparse.parse("($1,234,567.89)")
# => -1234567.89

import decimal

finparse.parse("$1,234,567.89", cast=decimal.Decimal)
# => Decimal('1234567.89')
```
