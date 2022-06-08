# BOJ 2108 통계학
import sys
from collections import Counter
def solution():
    n = int(input())
    numbers = list()
    for _ in range(n):
        numbers.append(int(sys.stdin.readline().rstrip()))
    numbers.sort()
    avg = round(sum(numbers) / n)
    med = numbers[n//2]
    mod = Counter(numbers).most_common()
    mod = sorted(mod, key=lambda x: x[1], reverse=True)
    if len(mod) > 1:
        if mod[0][1] == mod[1][1]:
            mod = mod[1][0]
        else:
            mod = mod[0][0]
    else:
        mod = mod[0][0]
    rng = abs(numbers[-1] - numbers[0])
    print(avg)
    print(med)
    print(mod)
    print(rng)


if '__main__' == __name__:
    solution()
