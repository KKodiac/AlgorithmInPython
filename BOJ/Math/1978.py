# BOJ 1978 소수 찾기
def solution():
    n = int(input())
    validate_numbers = list(map(int, input().split()))
    sieve_size = max(validate_numbers)
    primes = [True for _ in range(sieve_size+1)]
    primes[0] = primes[1] = False
    p = 2

    while p * p <= sieve_size:
        if primes[p]:
            for i in range(p*p, sieve_size+1, p):
                primes[i] = False
        p += 1

    answer = 0
    for number in validate_numbers:
        if primes[number]:
            answer += 1
    print(answer)


if '__main__' == __name__:
    solution()
