from random import choice


def random_placement(board, node):
    """
    Chooses a placement at random
    """
    available_placements = list(board.get_available_placements())
    return choice(available_placements)


def check_for_win_placement(board, node):
    """
    Checks if a placement can be made that leads to a win. If not, a node is chosen at random.
    """
    from pytro.game import get_winning_instance

    for available_placement in board.get_available_placements():
        potential_wins = get_winning_instance(
             board.dimensions(), board.get_rows(
                available_placement, candidate=node, min_length=board.height()))
        if len(potential_wins) > 0:
            # print('found potential win at', available_placement)
            return available_placement
    return random_placement(board, node)
