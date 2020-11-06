from board import Board

import os
import time


def main():
    board = Board.from_string("""
        ........................O..........................................................
        ......................O.O..........................................................
        ............OO......OO............OO...............................................
        ...........O...O....OO............OO...............................................
        OO........O.....O...OO.............................................................
        OO........O...O.OO....O.O..........................................................
        ..........O.....O.......O..........................................................
        ...........O...O...................................................................
        ............OO.....................................................................
        ...................................................................................
        ...................................................................................
        ...................................................................................
        ...................................................................................
        ...................................................................................
        ...................................................................................
        ...................................................................................
        ...................................................................................
        ...................................................................................
        ...................................................................................
    """)
    print(board)

    while True:
        try:
            time.sleep(0.1)
            board.next_generation()
            os.system('clear' if os.name == 'posix' else 'cls')
            print(board)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()

