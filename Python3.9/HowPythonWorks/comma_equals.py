"""
    , = 문법은 생소할 수도 있다.
    해당 문법은 
    x, y = y, x
    이렇게 패턴 매칭을 할 시 두 개의 요소를 사용하는 것을 볼 수 있는데,
    하나의 요소만 사용을 하면 
    x, = y
    이렇게 보여지게 된다.
"""

def do_something():
    """이미 r_value 가 iterable 의 하나 밖에 없는 값이라는 걸 알 시 사용"""
    primes = {2,3,5,7,11}
    evens = {2,4,6,8,10}

    x, = primes.intersection(evens)
    print(x)

if __name__ == '__main__':
    x = 1
    y = [2]
    # (x, y) = (y, x)
    x, = y
    print(x) # prints 2

    do_something()