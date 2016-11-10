# coding=utf-8

import finparse


def test_sign():
    assert finparse.sign_string('$5.00') == (1, '$5.00')
    assert finparse.sign_string('($5.00)') == (-1, '$5.00')
    assert finparse.sign_string('(($5.00))') == (1, '$5.00')
    assert finparse.sign_string('($5.00))') == (-1, '$5.00)')
    assert finparse.sign_string('(($5.00)') == (-1, '($5.00')
    assert finparse.sign_string('$100,000') == (1, '$100,000')
    assert finparse.sign_string('$100,000.') == (1, '$100,000.')
    assert finparse.sign_string('$100,000.111') == (1, '$100,000.111')
    assert finparse.sign_string('$100.000,') == (1, '$100.000,')


def test_strip():
    assert finparse.strip('$5.00') == '5.00'
    assert finparse.strip('($5.00)') == '5.00'
    assert finparse.strip('(($5.00))') == '5.00'
    assert finparse.strip('($5.00))') == '5.00'
    assert finparse.strip('(($5.00)') == '5.00'
    assert finparse.strip('$100,000') == '100000'
    assert finparse.strip('$100,000.') == '100000.'
    assert finparse.strip('$100,000.111') == '100000.111'
    assert finparse.strip('$100.000,', ',') == '100000,'


def test_parse():
    assert finparse.parse('$5.00') == 5.
    assert finparse.parse('($5.00)') == -5.
    assert finparse.parse('(($5.00))') == 5.
    assert finparse.parse('($5.00))') == -5.
    assert finparse.parse('(($5.00)') == -5.
    assert finparse.parse('$100,000') == 100000.
    assert finparse.parse('$100,000.') == 100000.
    assert finparse.parse('$100,000.111') == 100000.111
    assert finparse.parse('$100.000,', ',') == 100000.
    assert finparse.parse('1,234,567.89') == 1234567.89
    assert finparse.parse('1234567.89') == 1234567.89
    assert finparse.parse('1234567,89', ',') == 1234567.89
    assert finparse.parse('1,234,567·89', '·') == 1234567.89
    assert finparse.parse('1.234.567,89', ',') == 1234567.89
    assert finparse.parse('1˙234˙567,89', ',') == 1234567.89
    assert finparse.parse('1\'234\'567.89') == 1234567.89
    assert finparse.parse('1\'234\'567,89', ',') == 1234567.89
    assert finparse.parse('1.234.567’89', '’') == 1234567.89
    assert finparse.parse('1.234.567,89', ',') == 1234567.89
