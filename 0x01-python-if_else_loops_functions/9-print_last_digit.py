#!/usr/bin/python3
def print_last_digit(number):
    print('{:c}'.format((abs(int(number)) % 10) + ord('0')), end='')
    return abs(int(number)) % 10
