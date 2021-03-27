import numpy as np
from unittest import TestCase
from typing import *
import sys

if ".." not in sys.path:
    sys.path.append("..")

from src.basic import *

black, white, none = GoPlayer.black, GoPlayer.white, GoPlayer.none


def check_board_v0(case: TestCase, Board: Type[GoBoardBase]):
    b = Board(4)

    def test_grid(grid: List[List[GoPlayer]]):
        case.assertTrue(
            np.all(np.array(grid, np.uint8) == b.grid))

    case.assertTrue(np.all(np.full((4, 4), GoPlayer.none, np.uint8) == b.grid))
    b.play((0, 0), black)
    b.play((0, 1), white)
    b.play((1, 1), black)
    b.play((1, 0), white)
    test_grid([[none, white, none, none],
               [white, black, none, none],
               [none, none, none, none],
               [none, none, none, none]])
    case.assertRaises(GoIllegalActionError, lambda: b.play((0, 0), black))
    for i in range(4):
        for j in range(4):
            if 0 <= i < 2 and 0 <= j < 2:
                case.assertFalse(b.is_valid_point((i, j), black))
            else:
                case.assertTrue(b.is_valid_point((i, j), black))
    test_grid([[none, white, none, none],
               [white, black, none, none],
               [none, none, none, none],
               [none, none, none, none]])
    b.play((2, 0), black)
    b.play((1, 2), white)
    b.play((0, 2), black)
    b.play((3, 3), white)
    b.play((0, 0), black)
    test_grid([[black, none, black, none],
               [none, black, white, none],
               [black, none, none, none],
               [none, none, none, white]])

    b = Board(3)
    case.assertTrue(np.all(np.full((3, 3), GoPlayer.none, np.uint8) == b.grid))
    b.play((0, 1), black)
    b.play((0, 0), white)
    b.play((0, 2), black)
    b.play((2, 0), white)
    b.play((1, 2), black)
    test_grid([[white, black, black],
               [none, none, black],
               [white, none, none]])
    bs = b.get_string((0, 1))
    case.assertTrue(bs == b.get_string((0, 2)) == b.get_string((1, 2)))
    case.assertSetEqual({(0, 1), (0, 2), (1, 2)}, bs.stones)
    case.assertSetEqual({(1, 1), (2, 2)}, bs.liberties)
    case.assertEqual(GoPlayer.black, bs.player)
    ws1 = b.get_string((0, 0))
    ws2 = b.get_string((2, 0))
    case.assertSetEqual({(0, 0)}, ws1.stones)
    case.assertSetEqual({(1, 0)}, ws1.liberties)
    case.assertEqual(GoPlayer.white, ws1.player)
    case.assertSetEqual({(2, 0)}, ws2.stones)
    case.assertSetEqual({(1, 0), (2, 1)}, ws2.liberties)
    case.assertEqual(GoPlayer.white, ws2.player)

    b = Board(5)
    b.play((0, 0), black)
    b.play((0, 1), black)
    b.play((0, 2), black)
    b.play((0, 3), black)
    b.play((1, 3), black)
    b.play((2, 0), black)
    b.play((2, 1), black)
    b.play((2, 2), black)
    b.play((2, 3), black)
    b.play((1, 0), white)
    b.play((1, 2), white)

    test_grid([[black, black, black, black, none],
               [white, none, white, black, none],
               [black, black, black, black, none],
               [none, none, none, none, none],
               [none, none, none, none, none]])
    b._next_player = black
    case.assertTrue(b.is_valid_point((1, 1)))
    b._next_player = white
    case.assertFalse(b.is_valid_point((1, 1)))
