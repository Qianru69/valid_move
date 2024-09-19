from valid_move import isValidMove

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

def test_1():
    start = [0, 0]
    end = [0, 0]
    canIDoThis = isValidMove(test_board, start, end)

    assert canIDoThis == False
    print("Test 1 passed")

def test_2():
    start = [0, 0]
    end = [0, 3]
    canIDoThis = isValidMove(test_board, start, end)

    assert canIDoThis == False
    print("Test 2 passed")

def test_3():
    start = [3, 3]
    end = [0, 0]
    canIDoThis = isValidMove(test_board, start, end)

    assert canIDoThis == False
    print("Test 3 passed")

def test_4():
    start = [10, 3]
    end = [0, 1]
    canIDoThis = isValidMove(test_board, start, end)

    assert canIDoThis == False
    print("Test 4 passed")

def test_5():
    start = [1, 1]
    end = [2, 1]
    canIDoThis = isValidMove(test_board, start, end)

    assert canIDoThis == True
    print("Test 5 passed")

def test_6():
    start = [1, 2]
    end = [3, 3]
    canIDoThis = isValidMove(test_board, start, end)

    assert canIDoThis == False
    print("Test 6 passed")


test_board_1 = [
    ['R', 'H', 'B', 'K', 'Q', 'B', 'H', 'R'],
    ['.', '.', '.', 'P', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'p', '.', '.', '.', '.'],
    ['r', 'h', 'b', 'k', 'q', 'b', 'h', 'r']
]

def test_7():
    start = [0, 4]
    end = [5, 4]
    canIDoThis = isValidMove(test_board_1, start, end)

    assert canIDoThis == True
    print("Test 7 passed")

def test_8():
    start = [0, 4]
    end = [1, 2]
    canIDoThis = isValidMove(test_board_1, start, end)

    assert canIDoThis == False
    print("Test 8 passed")

def test_9():
    start = [0, 4]
    end = [1, 5]
    canIDoThis = isValidMove(test_board_1, start, end)

    assert canIDoThis == True
    print("Test 9 passed")

def test_10():
    start = [0, 4]
    end = [7, 4]
    canIDoThis = isValidMove(test_board_1, start, end)

    assert canIDoThis == True
    print("Test 10 passed")

