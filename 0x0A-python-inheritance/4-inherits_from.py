#!/usr/bin/python3
'''Defines inherits_from function.'''


def inherits_from(obj, a_class):
    '''Determines if an object is a true subclass of a class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
