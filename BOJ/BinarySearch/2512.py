# BOJ 2512 예산
import sys
def solution():
    n = int(sys.stdin.readline())
    request = list(map(int, sys.stdin.readline().rstrip().split()))
    budget = int(sys.stdin.readline().rstrip())
    start = 0
    end = max(request)

    while start <= end:
        mid = (end + start) // 2
        total = 0
        for r in request:
            if r <= mid:
                total += r
            else:
                total += mid

        if total <= budget:
            start = mid + 1
        else:
            end = mid - 1

    print(end)

if '__main__' == __name__:
    solution()