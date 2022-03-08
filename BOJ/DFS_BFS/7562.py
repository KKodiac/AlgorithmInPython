# BOJ 7562번 문제: 나이트의 이동
from collections import deque

possible_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

def solution():
    test_cases = int(input())
    
    for _ in range(test_cases):
        board_size = int(input())
        chess_board = [[0 for i in range(board_size)] for _ in range(board_size)]
        knight_position = list(map(int, input().split()))
        desired_position = list(map(int, input().split()))
        print(bfs(chess_board, knight_position[0], knight_position[1], desired_position[0], desired_position[1]))


def bfs(board, knight_X, knight_Y, desired_X, desired_Y):
    if knight_X == desired_X and knight_Y == desired_Y:
        return 0

    board[knight_X][knight_Y] = 1
    answer = 1
    stack = deque([(knight_X, knight_Y)])

    while stack:
        size = len(stack)
        for s in range(size):
            x, y = stack.popleft()
            for i in range(len(possible_moves)):
                new_X = x + possible_moves[i][0]
                new_Y = y + possible_moves[i][1]
                if new_X == desired_X and new_Y == desired_Y:
                    return answer
                elif 0 <= new_X < len(board) and 0 <= new_Y < len(board) and not board[new_X][new_Y]:
                    board[new_X][new_Y] = 1
                    stack.append((new_X, new_Y))
        answer += 1

    return answer


if '__main__' == __name__:
    solution()