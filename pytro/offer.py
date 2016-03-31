def random_pick(board, available_nodes):
    """
    Offers a node at random.
    """
    from random import randint

    index = randint(0, len(available_nodes) - 1)
    return index


def prevent_win_offer(board, available_nodes):
    """
    Offers a node and checks if the next player cannot win with this node. If only winning nodes are left, a node
    is chosen at random.
    """
    from pytro.game import get_winning_instance

    for node_index, node in enumerate(available_nodes):
        is_win = False
        for placement in board.get_available_placements():
            potential_wins = get_winning_instance(
                board.dimensions(), board.get_rows(
                    placement, candidate=node, min_length=board.height()))
            if len(potential_wins) > 0:
                is_win = True
        if not is_win:
            return node_index
    return random_pick(board, available_nodes)
