cpdef list _solve(list board, tuple p):
    cdef tuple new_p = _get_next_p(board, p)
    
    if not new_p:
        return True

    cdef int n = 0
    for n in range(1, 10):
        if _can_place(board, p, n):
            board[p[0]][p[1]] = n
            if _solve(board, new_p):
                return True

        # undo current point
        board[p[0]][p[1]] = 0


cpdef bint _empty_point(list board, tuple p):
    return board[p[0]][p[1]] == 0


cpdef tuple _get_next_p(list board, tuple p):
    if p[0] == 8 and p[1] == 8:
        if _empty_point(board, p):
            return p

        # no points left
        return None

    cdef tuple new_p = (p[0]+1, 0) if p[1] == 8 else (p[0], p[1]+1)

    if _empty_point(board, new_p):
        return new_p
    else:
        return _get_next_p(board, new_p)


cpdef bint _can_place(list board, tuple p, int n):
    # check horisontal and vertical
    cdef int i = 0
    for i in range(9):
        if board[p[0]][i] == n or board[i][p[1]] == n:
            return False

    cdef int x = 6
    cdef int y = 6

    if p[0] < 3:
        x = 0
    elif p[0] < 6:
        x = 3

    if p[1] < 3:
        y = 0
    elif p[1] < 6:
        y = 3
 
    # check square
    i = 0
    cdef int j = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            if board[i][j] == n:
                return False

    return True


cpdef solve_sudoku(list board):
    if len(board) != 9 or len(board[0]) != 9:
        raise ValueError('Wrong board')

    cdef list solved_board = board.copy()
    _solve(solved_board, (0,0))
    return solved_board
