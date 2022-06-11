# BOJ 9020 골드바흐의 추측
import sys
def solution():
    t = int(sys.stdin.readline())
    s = sieve()
    for _ in range(t):
        answer = (0, 0)
        n = int(sys.stdin.readline())

        for value, is_prime in enumerate(s[:n//2+1]):
            if is_prime:
                another_value = n - value
                if s[another_value]:
                    answer = (value, another_value)

        print(answer[0], answer[1])


def sieve():
    s = [True] * 10001
    s[0] = s[1] = False
    p = 2
    while p * p <= 10000:
        if s[p]:
            for i in range(p*p, 10000, p):
                s[i] = False
        p += 1

    return s


if '__main__' == __name__:
    solution()