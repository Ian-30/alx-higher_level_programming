#!/usr/bin/python3
"""Defines a class Square."""


class Square:

    def __init__(self, size=0):
    """Represents a square
     Attributes:
     __size (int): size of a side of the square
    """

    self.size = size

    def area(self):
        """
        Calculates the square's area
        Returns:The area of the square
        """

        return (self.__size) ** 2

    @property
    def size(self):
        """
         getter of __size
         Returns:The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
         setter of __size
         Args:
            value (int): size of a side of the square
        Returns:None
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """
        Prints the square
        Returns:None
        """

        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for k in range(self.__size)]))
