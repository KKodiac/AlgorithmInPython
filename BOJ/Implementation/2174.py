# BOJ 2174 로봇 시뮬레이션
import sys
input = sys.stdin.readline


def solution():
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    field = [[0] * a for _ in range(b)]
    is_error = False
    commands = {
        'L': 1,
        'R': -1,
        'F': 0
    }
    directions = {
        'N': 0,
        'W': 1,
        'S': 2,
        'E': 3,
    }
    directions_ = ['N', 'W', 'S', 'E']
    forward_action = {
        0: [-1, 0],
        1: [0, -1],
        2: [1, 0],
        3: [0, 1]
    }
    locations = []
    for robot in range(1, n+1):
        start_x, start_y, direction = input().split()
        start_x, start_y = int(start_x), int(start_y)
        r, c = b - int(start_y), int(start_x) - 1
        locations.append([r, c, direction])
        field[r][c] = robot

    for _ in range(m):
        robot, command, duration = input().split()
        robot, duration = int(robot), int(duration)
        r, c, d = locations[robot - 1]
        if command == 'F':
            fr, fc = forward_action[directions[d]]
            for i in range(1, duration+1):
                if 0 <= r+fr < b and 0 <= c+fc < a:
                    if field[r+fr][c+fc]:
                        print(f"Robot {robot} crashes into robot {field[r+fr][c+fc]}")
                        is_error = True
                        break
                    else:
                        field[r][c] = 0
                        r, c = r + fr, c + fc
                        field[r][c] = robot
                        locations[robot-1] = [r, c, d]
                else:
                    print(f"Robot {robot} crashes into the wall")
                    is_error = True
                    break
        else:
            duration %= 4
            nd = directions_[(directions[d] + commands[command] * duration) % 4]
            locations[robot - 1] = [r, c, nd]

        if is_error:
            break

    if not is_error:
        print('OK')

if '__main__' == __name__:
    solution()
