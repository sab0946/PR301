class Relationship:

    """Builds the class relationship data
    >>> a = Relationship(('extends', 'Class2'))
    >>> print(a.__name)
    Class2
    >>> print(a.__type)
    extends
    """

    def __init__(self, new_type):
        self.__name = new_type[1]
        self.__type = new_type[0]

    def __str__(self):
        return f"{self.__name}s"


if __name__ == "__main__":
    from doctest import testmod
    testmod()
