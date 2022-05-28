# BOJ 2960 에라토스테네스의 체
def solution():
    n, k = map(int, input().split())
    primes = [True for _ in range(n+1)]
    for i in range(2, n+1):
        p = primes[i]
        if p:
            p = False
            k -= 1
            for j in range(i*i, n+1, i):
                if primes[j]:
                    primes[j] = False
                    k -= 1
                    if not k:
                        print(j)
                        return
            if not k:
                print(i)
                return

if '__main__' == __name__:
    solution()