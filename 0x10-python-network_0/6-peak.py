#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    p = int(length / 2)
    li = list_of_integers

    if p - 1 < 0 and p + 1 >= length:
        return li[p]
    elif p - 1 < 0:
        return li[p] if li[p] > li[p + 1] else li[p + 1]
    elif m + 1 >= length:
        return li[p] if li[p] > li[p - 1] else li[p - 1]

    if li[p - 1] < li[p] > li[p + 1]:
        return li[p]

    if li[p + 1] > li[p - 1]:
        return find_peak(li[p:])
    return find_peak(li[:p])
