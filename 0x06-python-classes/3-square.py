#!/usr/bin/python3
"""Square module."""



class Square:
    """Defines a square."""

    def _init_(self, size=0):
        """Constructor.

        Args:
            size: Length of a sideof the square.
           
        Raises:
            TypeError: If size is not an integer.
            ValueError: IF size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._size = size
        
    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self._size ** 2
