from typing import List


class Board:
    __NO_CELL = False
    __CELL = True
    __DISPLAY_VALUES = {
        __NO_CELL: '.',
        __CELL: 'O',
    }

    __board: List[List[bool]]

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__board = [[self.__NO_CELL for col in range(width)] for row in range(height)]

    def next_generation(self) -> None:
        next_gen = []

        for row_idx, row in enumerate(self.__board):
            next_gen.append([])
            for col_idx, cell in enumerate(row):
                neighbours_count = self._get_neighbours(row_idx, col_idx)
                should_live = neighbours_count == 3 or (cell and neighbours_count == 2)
                next_gen[-1].append(should_live)

        self.__board = next_gen

    def _get_neighbours(self, row: int, col: int):
        neighbours = 0

        # NOTE(yavor): if this confuses you, see the commit, it's simpler
        # and equivalent
        # Basically we have to generate each surrounding coordinates of the matrix
        # (-1, -1); (-1, 0); (-1, 1); (0, -1); (0, 1) and so on
        directions = [(delta_y, delta_x) for delta_x in [1, 0, -1] for delta_y in [1, 0, -1]]
        directions = [d for d in directions if d != (0, 0)]
        for delta_row, delta_col in directions:
            target_row, target_col = row + delta_row, col + delta_col
            if not (0 <= target_row < self.__height):
                continue
            if not (0 <= target_col < self.__width):
                continue
            neighbours += int(self.__board[target_row][target_col])

        return neighbours

    def spawn_cell(self, row: int, col: int):
        self.__board[row][col] = self.__CELL

    def kill_cell(self, row: int, col: int):
        self.__board[row][col] = self.__NO_CELL

    @classmethod
    def from_string(cls, string_repr: str) -> 'Board':
        rows = string_repr.strip('\n \t').split('\n')
        board = Board(height=len(rows), width=len(rows[0]))

        for row_idx, row in enumerate(rows):
            for col_idx, cell_repr in enumerate(row.strip()):
                if cell_repr != cls.__DISPLAY_VALUES[cls.__NO_CELL]:
                    board.spawn_cell(row_idx, col_idx)

        return board

    @classmethod
    def from_file(cls, file_name: str) -> 'Board':
        with open(file_name) as f:
            lines = f.readlines()
            cls.from_string('\n'.join(lines))

    def __str__(self) -> str:
        rows = [' '.join([self.__DISPLAY_VALUES[col] for col in row]) for row in self.__board]

        return '\n'.join(rows)

    def _print_row(self, row_idx):
        print(self.__board[row_idx])
