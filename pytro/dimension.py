
class Dimension(object):
    """
    A dimension specifies the type of an attribute.
    """

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return str(self.__name)

    def __eq__(self, other):
        return self.__name == other.__name
