# BOJ 1931번 문제: 회의실 배정
def solution():
    N = int(input())
    room = list()
    for i in range(N):
        a, b = map(int, input().split())
        room.append((a,b))

    room.sort(key=lambda x: (x[1], x[0]))

    end_time = room[0][1]
    answer = 1
    for j in range(N):
        if end_time <= room[j][0]:
            end_time = room[j][1]
            answer += 1

    print(answer)


if '__main__' == __name__:
    solution()
