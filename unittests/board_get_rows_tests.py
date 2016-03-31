import unittest
from pytro.board import Board


class TestBoardGetRows(unittest.TestCase):
    """
    Unit tests for Board.get_rows
    """

    def test_single_horizontal_row_start_left(self):
        board = Board(5, 5)
        board.add_node(1, 2, 'n1').add_node(2, 2, 'n2').add_node(3, 2, 'n3')

        result = board.get_rows((1, 2))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n1', 'n2', 'n3'])

    def test_single_horizontal_row_start_right(self):
        board = Board(5, 5)
        board.add_node(1, 2, 'n1').add_node(2, 2, 'n2').add_node(3, 2, 'n3')

        result = board.get_rows((3, 2))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n1', 'n2', 'n3'])

    def test_single_horizontal_row_start_middle(self):
        board = Board(5, 5)
        board.add_node(1, 2, 'n1').add_node(2, 2, 'n2').add_node(3, 2, 'n3')

        result = board.get_rows((2, 2))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n1', 'n2', 'n3'])

    def test_single_vertical_row_start_up(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(1, 2, 'n2').add_node(1, 3, 'n3')

        result = board.get_rows((1, 1))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n1', 'n2', 'n3'])

    def test_single_vertical_row_start_down(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(1, 2, 'n2').add_node(1, 3, 'n3')

        result = board.get_rows((1, 3))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n1', 'n2', 'n3'])

    def test_single_vertical_row_start_middle(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(1, 2, 'n2').add_node(1, 3, 'n3')

        result = board.get_rows((1, 2))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n1', 'n2', 'n3'])

    def test_mixed_rows_start_upper_left(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(1, 2, 'n2').add_node(1, 3, 'n3')
        board.add_node(2, 1, 'n4').add_node(3, 1, 'n5')

        result = board.get_rows((1, 1))
        self.assertEqual(len(result), 2)
        self.assertTrue(['n1', 'n2', 'n3'] in result)
        self.assertTrue(['n1', 'n4', 'n5'] in result)

    def test_mixed_rows_start_lower_left(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(1, 2, 'n2').add_node(1, 3, 'n3')
        board.add_node(2, 3, 'n4').add_node(3, 3, 'n5')

        result = board.get_rows((1, 3))
        self.assertEqual(len(result), 2)
        self.assertTrue(['n1', 'n2', 'n3'] in result)
        self.assertTrue(['n3', 'n4', 'n5'] in result)

    def test_mixed_rows_start_upper_right(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(2, 1, 'n2').add_node(3, 1, 'n3')
        board.add_node(3, 2, 'n4').add_node(3, 3, 'n5')

        result = board.get_rows((3, 1))
        self.assertEqual(len(result), 2)
        self.assertTrue(['n1', 'n2', 'n3'] in result)
        self.assertTrue(['n3', 'n4', 'n5'] in result)

    def test_mixed_rows_start_lower_right(self):
        board = Board(5, 5)
        board.add_node(3, 1, 'n1').add_node(3, 2, 'n2').add_node(3, 3, 'n3')
        board.add_node(2, 3, 'n4').add_node(1, 3, 'n5')

        result = board.get_rows((3, 3))
        self.assertEqual(len(result), 2)
        self.assertTrue(['n1', 'n2', 'n3'] in result)
        self.assertTrue(['n5', 'n4', 'n3'] in result)

    def test_mixed_rows_start_middle(self):
        board = Board(5, 5)
        board.add_node(3, 1, 'n1').add_node(3, 2, 'n2').add_node(3, 3, 'n3')
        board.add_node(2, 2, 'n4').add_node(4, 2, 'n5')

        result = board.get_rows((3, 2))
        self.assertEqual(len(result), 2)
        self.assertTrue(['n1', 'n2', 'n3'] in result)
        self.assertTrue(['n4', 'n2', 'n5'] in result)

    def test_smaller_than_min_length_is_filtered(self):
        board = Board(5, 5)
        board.add_node(3, 1, 'n1').add_node(3, 2, 'n2').add_node(3, 3, 'n3')
        board.add_node(2, 2, 'n4')

        result = board.get_rows((3, 2), min_length=3)
        self.assertEqual(len(result), 1)
        self.assertTrue(['n1', 'n2', 'n3'] in result)

    def test_stop_on_upwards_gap(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(1, 3, 'n2').add_node(1, 4, 'n3')

        result = board.get_rows((1, 4))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n2', 'n3'])

    def test_stop_on_downwards_gap(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(1, 2, 'n2').add_node(1, 4, 'n3')

        result = board.get_rows((1, 1))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n1', 'n2'])

    def test_stop_on_left_gap(self):
        board = Board(5, 5)
        board.add_node(1, 1, 'n1').add_node(2, 1, 'n2').add_node(4, 1, 'n3')

        result = board.get_rows((1, 1))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n1', 'n2'])

    def test_stop_on_right_gap(self):
        board = Board(5, 5)
        board.add_node(4, 1, 'n1').add_node(3, 1, 'n2').add_node(1, 1, 'n3')

        result = board.get_rows((4, 1))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['n2', 'n1'])


if __name__ == '__main__':
    unittest.main()
