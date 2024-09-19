from valid_move import *
from tests import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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