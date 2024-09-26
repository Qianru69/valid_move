def isValidMove(board, starting_pos, ending_pos):
    # Check if the starting position and ending position are the same
    #if starting_pos == ending_pos:
    #    return False

    # Check if the starting position is a valid position on the board
    if not validPos(board, starting_pos, ending_pos):
        return False

    start_piece = getPiece(board, starting_pos)
    ending_pos_piece = getPiece(board, ending_pos)

    # Check if the ending position is valid
    if ending_pos_piece[0] != None:
        if ending_pos_piece[1] == start_piece[1]:
            return False

    # Check if the piece is a pawn
    if start_piece[0] == 'P' or start_piece[0] == 'p':
        return checkPawn(starting_pos, ending_pos, start_piece[1])

    if start_piece[0] == 'Q' or start_piece[0] == 'q':
        return checkQueen(starting_pos, ending_pos)

    return True

def validPos(board, start_pos, end_pos):
    if not validPosOnBoard(start_pos) or not validPosOnBoard(end_pos):
        return False

    # Check if the starting position is empty
    if board[start_pos[0]][start_pos[1]] == '.':
        return False

    return True

def validPosOnBoard(pos):
    # Check if the position is a valid position on the board
    if pos[0] < 0 or pos[1] < 0 or pos[0] > 7 or pos[1] > 7:
        print("Invalid position")
        return False

    return True

def getPiece(board, pos):
    if board[pos[0]][pos[1]] == '.':
        return (None, None)

    piece, color = None, None
    # Check what is the piece on the position
    piece = board[pos[0]][pos[1]]
    # check the piece is by white or black
    if piece.isupper():
        color = 'WHITE'
    else:
        color = 'BLACK'

    return (piece, color)

def checkPawn(starting_pos, ending_pos, color):
    # Check if the pawn is moving in the right direction
    if color == 'WHITE':
        if ending_pos[0] - starting_pos[0] != 1:
            return False
    else:
        if starting_pos[0] - ending_pos[0] != 1:
            return False

    # Check if the pawn is moving forward
    if starting_pos[1] == ending_pos[1]:
        return True

    # Check if the pawn is moving diagonally
    if abs(starting_pos[1] - ending_pos[1]) == 1:
        return True

    return False

def checkQueen(starting_pos, ending_pos):
    if starting_pos[0] == ending_pos[0] or starting_pos[1] == ending_pos[1]:
        return True

    if abs(starting_pos[0] - ending_pos[0]) == abs(starting_pos[1] - ending_pos[1]):
        return True

    return False


