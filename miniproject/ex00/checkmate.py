def checkmate(board: str):
    lines = board.strip().split("\n")
    size = len(lines)
    
    king_pos = None
    for row in range(size):
        for col in range(size):
            if lines[row][col] == 'K':
                king_pos = (row, col)
                break
        if king_pos:
            break
    
    if not king_pos:
        print("Error")
        return

    kx, ky = king_pos

    def check_pawn():
        if kx > 0:
            if ky > 0 and lines[kx - 1][ky - 1] == 'P':
                return True
            if ky < size - 1 and lines[kx - 1][ky + 1] == 'P':
                return True
        return False

    def check_straight(dx, dy, piece):
        x, y = kx + dx, ky + dy
        while 0 <= x < size and 0 <= y < size:
            if lines[x][y] != '.':
                return lines[x][y] == piece
            x += dx
            y += dy
        return False

    def check_diagonal(dx, dy, piece):
        x, y = kx + dx, ky + dy
        while 0 <= x < size and 0 <= y < size:
            if lines[x][y] != '.':
                return lines[x][y] == piece
            x += dx
            y += dy
        return False

    if check_pawn() or \
       check_straight(1, 0, 'R') or check_straight(-1, 0, 'R') or \
       check_straight(0, 1, 'R') or check_straight(0, -1, 'R') or \
       check_diagonal(1, 1, 'B') or check_diagonal(-1, -1, 'B') or \
       check_diagonal(1, -1, 'B') or check_diagonal(-1, 1, 'B') or \
       check_straight(1, 0, 'Q') or check_straight(-1, 0, 'Q') or \
       check_straight(0, 1, 'Q') or check_straight(0, -1, 'Q') or \
       check_diagonal(1, 1, 'Q') or check_diagonal(-1, -1, 'Q') or \
       check_diagonal(1, -1, 'Q') or check_diagonal(-1, 1, 'Q'):
        print("Success")
    else:
        print("Fail")


    
