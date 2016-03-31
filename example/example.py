from pytro.board import Board
from pytro.dimension import Dimension
from pytro.game import play
from pytro.node import create_nodes
from pytro.placement import random_placement, check_for_win_placement
from pytro.offer import prevent_win_offer, random_pick

from collections import Counter

nodes = list(
    create_nodes(
        dict(
            height=['small', 'big'],
            color=['red', 'blue'],
            form=['round', 'squared'],
            surface=['smooth', 'rough']
        )
    )
)

dimensions = [Dimension('height'),  Dimension('color'), Dimension('form'),  Dimension('surface')]
board_size = 4

p1 = {'id': 'P1', 'placement_strategy': check_for_win_placement, 'offer_strategy': prevent_win_offer}
p2 = {'id': 'P2', 'placement_strategy': check_for_win_placement, 'offer_strategy': prevent_win_offer}
p3 = {'id': 'P3', 'placement_strategy': check_for_win_placement, 'offer_strategy': prevent_win_offer}

player = [p1, p2]


def event_bus(context, *args):
    # print(context, *args)
    pass

win_counter = Counter()
for i in range(0, 1000):
    result = play(board=Board(width=board_size, height=board_size, dimensions=dimensions),
                  nodes=nodes,
                  players=player,
                  event_bus=event_bus)
    if 'winner' in result:
        win_counter.update([result['winner']['id']])
    else:
        win_counter.update(['tie'])

print(win_counter)


