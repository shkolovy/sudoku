def _solve(board, p):
    new_p = _get_next_p(board, p)
    
    if not new_p:
        return True

    # try to put number from 1 to 9
    for n in range(1, 10):
        if _can_place(board, p, n):
            board[p[0]][p[1]] = n
            if _solve(board, new_p):
                return True

        # undo current point
        board[p[0]][p[1]] = 0


def _empty_point(board, p):
    return board[p[0]][p[1]] == 0


def _get_next_p(board, p):
    if p[0] == 8 and p[1] == 8:
        if _empty_point(board, p):
            return p

        # no points left
        return None

    new_p = (p[0]+1, 0) if p[1] == 8 else (p[0], p[1]+1)

    if _empty_point(board, new_p):
        return new_p
    else:
        return _get_next_p(board, new_p)


def _can_place(board, p, n):
    # check horisontal and vertical
    for i in range(9):
        if board[p[0]][i] == n or board[i][p[1]] == n:
            return False

    x, y = 3*(p[0]//3), 3*(p[1]//3)
 
    # check square
    for i in range(x, x+3):
        for j in range(y, y+3):
            if board[i][j] == n:
                return False

    return True

# TODO: add exception if board can be soved
def solve(board):
    """
    Solve sudoku. Empty cells shoud be '0'
    board: 2d list 9X9
    """

    if len(board) != 9 or len(board[0]) != 9:
        raise ValueError('Wrong board')

    solved_board = board.copy()
    _solve(solved_board, (0,0))
    return solved_board

# TODO: impement it
def check(board):
    pass


# ar = [[0, 2, 0, 8, 0, 0, 0, 9, 0],
#       [0, 0, 0, 1, 0, 0, 7, 0, 5],
#       [0, 0, 0, 0, 4, 7, 0, 6, 0],
#       [0, 0, 2, 0, 0, 0, 9, 0, 0],
#       [0, 0, 0, 0, 5, 3, 0, 0, 0],
#       [0, 3, 0, 4, 0, 0, 1, 0, 0],
#       [9, 0, 0, 0, 0, 0, 0, 0, 6],
#       [0, 0, 7, 0, 1, 0, 0, 0, 3],
#       [0, 0, 3, 7, 0, 2, 0, 0, 0]]


# import pprint
# pprint.pprint(solve(ar))