
class Attribute(object):
    """
    Attribute of a node. An attribute has a dimension (e.g. color or form) and a value (e.g. blue or squared)
    """

    def __init__(self, dimension, value):
        self.dimension = dimension
        self.value = value

    def __str__(self):
        return str(self.dimension) + ':' + str(self.value)

    def __repr__(self):
        return str(self)
