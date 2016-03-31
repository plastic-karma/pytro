from pytro.attribute import Attribute
from itertools import product


class Node(object):
    """
    Represents a node that can be placed on a board. A node has a list of attributes.
    """

    def __init__(self, attributes):
        self.__attributes = attributes

    def __str__(self):
        return '{' + ','.join([str(attribute) for attribute in self.__attributes]) + '}'

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        for attribute in self.__attributes:
            if attribute.dimension == item:
                return attribute.value


def create_node(*args):
    """
    Creates a node.
    :param args: List of (dimension, value) attribute tuples.
    :return:
    """
    return Node([Attribute(dimension, value) for dimension, value in args])


def create_nodes(dimensions):
    """
    Creates a list of nodes with every combination of the given dimensions
    :param dimensions: dictionary of 'dimension' : [list of possible values]
    """
    from pytro.dimension import Dimension
    all_attributes = []
    for dimension_name, values in dimensions.items():
        attributes = []
        dimension = Dimension(dimension_name)
        for value in values:
                attributes.append(Attribute(dimension, value))
        all_attributes.append(attributes)

    return list([Node(attributes) for attributes in product(*all_attributes)])
