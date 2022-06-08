# BOJ 1929 소수 구하기 
def solution():
    m, n = map(int, input().split())
    primes = [True for _ in range(n+1)]
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False

        p += 1

    for i in range(m, n+1):
        if primes[i]:
            print(i)

if '__main__' == __name__:
    solution()