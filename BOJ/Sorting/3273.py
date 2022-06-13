# BOJ 3273 두 수의 합
from collections import defaultdict
def solution():
    n = int(input())
    sequence = list(map(int, input().split()))
    x = int(input())

    table = defaultdict(int)
    for seq in sequence:
        table[seq] = 1
    answer = 0
    for i in range(len(sequence)):
        num = x - sequence[i]
        if table[num]:
            answer += 1

    print(answer//2)


if '__main__' == __name__:
    solution()