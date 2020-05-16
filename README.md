# Finparse

![pypi](https://img.shields.io/pypi/v/finparse?color=yellow&logo=python&logoColor=eee&style=flat-square)
![python](https://img.shields.io/pypi/pyversions/finparse?logo=python&logoColor=eee&style=flat-square)
[![pytest](https://img.shields.io/github/workflow/status/amancevice/finparse/pytest?logo=github&style=flat-square)](https://github.com/amancevice/finparse/actions)
[![coverage](https://img.shields.io/codeclimate/coverage/amancevice/finparse?logo=code-climate&style=flat-square)](https://codeclimate.com/github/amancevice/finparse/test_coverage)
[![maintainability](https://img.shields.io/codeclimate/maintainability/amancevice/finparse?logo=code-climate&style=flat-square)](https://codeclimate.com/github/amancevice/finparse/maintainability)

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

## Pandas

Pandas' `read_csv()` function provdides a `converters` argument that applies a function to the given column.

Using the example CSV file [`./tests/example.csv`](./tests/example), we can see the following behavior:

```python
import pandas

df = pandas.read_csv('./tests/example.csv')

print(df)
# =>        Acct     Balance
#    0   Savings  $1,234.567
#    1  Checking    ($0.987)
```

With the `converters` argument we can parse these values to floats:

```python
import finparse
import pandas

df = pandas.read_csv('./tests/example.csv', converters={'Balance': finparse.parse})

print(df)
# =>        Acct   Balance
#    0   Savings  1234.567
#    1  Checking    -0.987
```
