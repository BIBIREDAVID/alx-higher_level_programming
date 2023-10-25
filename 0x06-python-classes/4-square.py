#!/usr/bin/python3
"""Square module."""


class Square:
    """DEfines a square."""
    def _init_(self, size=0):
        """Constructor.

        Args:
            size: Lenght of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the lenght of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._size = value

    def area(self):
        """Area of this square.

        Retutns:The size squared.
        """
        return self._size ** 2
