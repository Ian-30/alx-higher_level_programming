#!/usr/bin/python3
'''Defines a  MyList class.'''


class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))
