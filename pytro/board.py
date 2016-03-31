from itertools import product


class Board(object):
    """
    The game board, where nodes can be placed on.
    """

    def __init__(self, height, width, dimensions=None):
        """
        Creates a new game board.
        :param height: the height of the board. Must be a positive integer.
        :param width: the width of the board. Must be a positive integer.
        :param dimensions: list of dimensions, that are valid for this board
        :return: a new game board
        """
        if dimensions is None:
            dimensions = []
        self.__height = height
        self.__width = width
        self._dimensions = dimensions
        self.__nodes = {}

    def add_node(self, x, y, node):
        """
        Adds a node to the given coordinates on the board
        """
        self.__nodes[(x, y)] = node
        return self

    def dimensions(self):
        """
        Returns the valid dimensions for this board.
        """
        return self._dimensions

    def height(self):
        """
        Returns the height of this board.
        """
        return self.__height

    def get_available_placements(self):
        """
        Returns the available placements (in (x,y) coordinates) where nodes can be placed on.
        """
        for p in product(range(0, self.__width), range(0, self.__height)):
            if p not in self.__nodes:
                yield p

    def get_rows(self, coordinates, min_length=2, candidate=None):
        """
        Returns connected nodes. From the starting point we will check up, down left and right.
        Will return at most 2 lists. One for the x-axis, one for the y-axis.
        :param coordinates: starting point to check for
        :param min_length: all connected rows smaller than this value will be ignored
        :param candidate: Optional candidate to be placed on the given coordinates. Can be used to check if a placement
        would return in a row.
        """
        x, y = coordinates

        def set_candidate(result):
            if candidate is None:
                result.append(self.__nodes[coordinates])
            else:
                result.append(candidate)

        # check horizontal
        horizontal_result = []

        # check left
        for i in range(x - 1, -1, -1):
            if (i, y) in self.__nodes:
                prefix = [self.__nodes[(i, y)]]
                prefix.extend(horizontal_result)
                horizontal_result = prefix
            else:
                break

        set_candidate(horizontal_result)

        # check right
        for i in range(x + 1, self.__width):
            if (i, y) in self.__nodes:
                horizontal_result.append(self.__nodes[(i, y)])
            else:
                break

        # check vertically
        vertical_result = []

        # check up
        for j in range(y - 1, -1, -1):
            if(x, j) in self.__nodes:
                prefix = [self.__nodes[(x, j)]]
                prefix.extend(vertical_result)
                vertical_result = prefix
            else:
                break

        set_candidate(vertical_result)

        # check down
        for j in range(y + 1, self.__height):
            if (x, j) in self.__nodes:
                vertical_result.append(self.__nodes[(x, j)])
            else:
                break

        return list([l for l in [horizontal_result, vertical_result] if len(l) >= min_length])
