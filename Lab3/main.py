class KnightsTour:

    EMPTY = ' '
    JUMPS = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

    def __init__(self, row = 0, column = 0):
        self.current_move = 0
        self.solved = False
        self.board = []
        for row in range(8):
            self.board.append([])
            for square in range(8):
                self.board[row].append(KnightsTour.EMPTY)
        self.solve(row, column)

    def can_move_to(self, row, column):
        return 0 <= row < len(self.board)  \
            and 0 <= column < len(self.board) \
            and self.board[row][column] == KnightsTour.EMPTY \
            and not self.solved

    def solve(self, row, column):
        self.current_move += 1
        self.board[row][column] = self.current_move

        if self.current_move == len(self.board)**2:
            self.solved = True
            return

        positions = [Position(self, row+jump[0], column+jump[1]) for jump in KnightsTour.JUMPS ]
        positions.sort()
        for position in positions:
            if self.can_move_to(position.row, position.col):
                self.solve(position.row, position.col)

        if self.solved:
            return
        self.current_move -= 1
        self.board[row][column] = KnightsTour.EMPTY

    def __str__(self):
        return "\n".join(str(row) for row in self._board)

    def is_solved(self):
        return self._current_step == 64

    def can_move_to(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8 and self._board[row][col] == ' ' and not self.is_solved()

    def solve(self, row, col):
        self._board[row][col] = self._current_step
        if self.is_solved():
            print(self)
        else:
            next_moves = []
            for move in KnightsTour.POSSIBLE_MOVES:
                if self.can_move_to(row+move[0], col+move[1]):
                    next_moves.append(Position(self, row+move[0], col+move[1] ))
            next_moves.sort()
            for move in next_moves:
                self._current_step += 1
                self.solve(move.row, move.col)
                if not self.is_solved():
                    self._current_step -= 1
                    self._board[row][col] = ' '
                else:
                    return



class Position:

    def __init__(self, knights_tour, row, col):
        self.knights_tour = knights_tour
        self.row = row
        self.col = col

    def valid_moves(self):
        moves = 0
        for jump in KnightsTour.JUMPS:
            if self.knights_tour.can_move_to(self.row+jump[0], self.col+jump[1]):
                moves += 1
        return moves

        return moves

    def __lt__(self, other):
        return self.valid_moves() < other.valid_moves()

    def __gt__(self, other):
        return self.valid_moves() > other.valid_moves()

    def __eq__(self, other):
        return self.valid_moves() == other.valid_moves()

for row in range(8):
    for col in range(8):
        print("knights tour at {} {}".format(row, col))
        tour = KnightsTour(row, col)
        print()
