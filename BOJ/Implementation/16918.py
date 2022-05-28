# BOJ 16918 봄버맨
def solution():
    r, c, n = map(int, input().split())
    board = []
    for i in range(r):
        board_row = str(input())
        for j in range(c):
            row = [True if i == 'O' else False for i in board_row]
        board.append(row)

    area_of_impact = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    board_one = board
    board_two =


if '__main__' == __name__:
    solution()
