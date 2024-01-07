#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    for i in text:
        if c == 0:
            if i == ' ':
                continue
            else:
                c = 1
        if c == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                c = 0
            else:
                print(i, end="")
