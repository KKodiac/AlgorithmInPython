# BOJ 2581 소수


def solution():
    m = int(input())
    n = int(input())

    prime = [True for i in range(n + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    range_primes = []
    for p in range(m, n+1):
        if prime[p]:
            range_primes.append(p)

    if range_primes:
        print(sum(range_primes))
        print(range_primes[0])
    else:
        print(-1)

if '__main__' == __name__:
    solution()