import string


class GameBoard:
    legalValues = []

    def __init__(self, size):
        self.size = size
        self.allSpaces = []
        self.board = self.init_board()

    def init_board(self):
        board = []
        for y in range(self.size):
            line = []
            for x in range(self.size):
                line.append(' ')
                self.allSpaces.append([x, y])
            board.append(line)
        return board

    def set_values(self, values):
        self.legalValues = values

    def get_values(self):
        return self.legalValues

    def show_map(self):
        sep_coords = '\n   '

        for i in range(self.size):
            if i < 10:
                sep_coords += '| ' + str(i) + ' '
            else:
                sep_coords += '| ' + str(i) + ''
        sep_coords += '|'

        def col_index(i):
            return list(string.ascii_lowercase)[i]

        sep = '\n' + '---' + '+---' * self.size + '+\n'
        board = sep_coords + sep
        for y in range(self.size):
            board += ' ' + col_index(y) + ' '
            for x in range(self.size):
                board += '| ' + str(self.board[y][x]) + ' '
            board += '|'
            board += sep
        print(board)

    def set(self, x, y, value):
        self.board[y][x] = value

    def get(self, x, y):
        return self.board[y][x]
