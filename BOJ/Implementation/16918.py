# BOJ 16918 봄버맨
from typing import List


def solution():
    def print_board(board: List, row: int, col: int):
        for r in range(row):
            for c in range(col):
                if board[r][c]:
                    print('O', end='')
                else:
                    print('.', end='')
            print()

    def find_board_states(org: List, row: int, col: int):
        area_of_impact = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        part = [[True for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if org[r][c]: # Bomb
                    part[r][c] = False
                    for area in area_of_impact:
                        x = r + area[0]
                        y = c + area[1]
                        if 0 <= x < row and 0 <= y < col:
                            part[x][y] = False

        return part

    r, c, n = map(int, input().split())

    original_board = []  # 0
    for i in range(r):
        board_row = str(input())
        for j in range(c):
            row = [True if i == 'O' else False for i in board_row]
        original_board.append(row)
    full_board = [[True for _ in range(c)] for _ in range(r)]

    current_board = original_board
    if n == 1:
        print_board(current_board, r, c)
    elif n % 2 == 0:
        print_board(full_board, r, c)
    elif n % 4 == 3:
        current_board = find_board_states(current_board, r, c)
        print_board(current_board, r, c)
    elif n % 4 == 1:
        current_board = find_board_states(current_board, r, c)
        current_board = find_board_states(current_board, r, c)
        print_board(current_board, r, c)


if '__main__' == __name__:
    solution()
