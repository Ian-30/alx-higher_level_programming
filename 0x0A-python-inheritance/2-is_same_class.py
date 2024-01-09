#!/usr/bin/python3
'''Defines is_same_class function.'''


def is_same_class(obj, a_class):
    '''Determines if an object is an instance of a class.'''
    return type(obj) == a_class
