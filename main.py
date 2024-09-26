from valid_move import *
from tests import *

def generic_move(xs, ys, xe, ye):
    # figure out the direction of the move
    # no if statements
    # no loops

    return ((xe - xs)/abs((xs - xe)), (ye - ys)/abs(ys - ye))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(generic_move(1, 1, 2, 2))
    print(generic_move(2, 2, 1, 1))
    print(generic_move(1, 2, 2, 1))
    print(generic_move(2, 1, 1, 2))

    """
    test_board = [
    ['R', 'H', 'B', 'K', 'Q', 'B', 'H', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'k', 'q', 'b', 'h', 'r']
    ]

    start = [0, 1]
    end = [2, 2]
    canIDoThis = isValidMove(test_board, start, end)

    print(canIDoThis)

    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()
    test_10()
    """