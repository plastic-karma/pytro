
def play(board, nodes, players, event_bus):
    """
    This function is the actual game engine. Calling it represents a single game. Player one starts to offer a node to
    the next player. The next player places that node on the board and then offers a node to the next player. This
    continues until either all nodes are placed or one player places a node which results in a row of nodes which have
    have the same values for a single dimension, thus winning the game.

    :param board: The board on which the game is played
    :param nodes: The available nodes which can be used in the game
    :param players: a list of players. A player is a map with an 'id', a 'placement_strategy' which is
     a function(board, node) that returns a x,z coordinate pair and a 'offer_strategy' which is a function(board, nodes)
     that returns the index of the node that shall be offered to the next player.
    :param event_bus: function(context, *args) that will take game events, which can be logged or saved or ignored.
    :return: Returns a map with the optional attribute 'winner'. If 'winner' is not set, nobody won.
    """

    def player_rotation(player_list):
        while True:
            yield from player_list

    game_result = {}
    current_nodes = nodes[:]

    offer = None
    for current_player in player_rotation(players):
        player_id = current_player['id']
        if offer is not None:
            placement = current_player['placement_strategy'](board, offer)
            board.add_node(placement[0], placement[1], offer)
            event_bus(player_id, 'placing ', offer, 'on', placement)

            winning_row = get_winning_instance(board.dimensions(), board.get_rows(placement, min_length=board.height()))
            if len(winning_row) > 0:
                event_bus(player_id, 'won with ', winning_row)
                game_result['winner'] = current_player
                break

        if len(current_nodes) is 0 or board.get_available_placements() is 0:
            break

        offer_index = current_player['offer_strategy'](board, current_nodes)
        offer = current_nodes[offer_index]
        del current_nodes[offer_index]
        event_bus(player_id, 'offers', offer)

    return game_result


def get_winning_instance(dimensions, rows):
        """
        Returns a row of nodes, which have the same value for a given dimension. If no row has this property an empty
        list is returned.
        :param dimensions the valid dimensions to check for
        :param a list of rows
        """
        def dimension_is_singular(dimension, current_nodes):
            return len(set([node[dimension] for node in current_nodes])) == 1

        for connected_nodes in rows:
            for dim in dimensions:
                if dimension_is_singular(dim, connected_nodes):
                    return connected_nodes
        return []
