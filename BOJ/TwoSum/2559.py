# BOJ 2559 수열
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    temperature = list(map(int, input().split()))
    answer = sum(temperature[:k])
    old_sum = sum(temperature[:k])
    for i in range(n-k):
        new_sum = old_sum - temperature[i] + temperature[i+k]
        answer = max([old_sum, new_sum, answer])
        old_sum = new_sum

    print(answer)


if '__main__' == __name__:
    solution()
