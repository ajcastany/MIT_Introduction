#!/usr/bin/env python3
"""
Exercise 9 of the MIT Introduction to CS with Python.
================================================================================
Write a function that accepts two string as arguments and returns True if either string
occurs anywhere in the other and False otherwise.
Hint: use ~str~ built-in operation.

"""
String1 = "asdf"
String2 = "asdf afdfd"

def StringInString(x, y):
    if x in y or y in x:
        return True
    else:
        return False
