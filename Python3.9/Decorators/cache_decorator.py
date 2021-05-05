from functools import cache, lru_cache

"""
    `cache` decorator 은 이미 계산 된 내용을 메모리에 캐싱해서 이후 연산에 사용합니다.
"""
@cache
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

"""
    `lru_cache` decorator 은 `cache`가 메모리를 많이 사용하게 되기 때문에 
    maxsize로 지정 된 갯수 이상이 캐싱되면, 
    메모리에 캐싱 된 least recently used 요소를 삭제 하며 메모리 사용을 최소화 할 수 있습니다.
"""
@lru_cache(maxsize=5)
def fib_lru(n):
    if n <= 1:
        return n

    return fib_lru(n - 1) + fib_lru(n - 2)

"""
    캐싱을 사용하지 않은 recursive 피보다치 코드
"""
def fib_none(n):
    if n <= 1:
        return n

    return fib_none(n - 1) + fib_none(n - 2)

if __name__ == '__main__':
    # cache decorator
    for i in range(400):
        print(i, fib(i))

    # lru_cache decorator
    for i in range(400):
        print(i, fib_lru(i))

    # nothing, just plain recursion
    for i in range(400):
        print(i, fib_none(i))

    