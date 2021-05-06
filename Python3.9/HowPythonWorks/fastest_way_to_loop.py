"""
    파이썬으로 Looping 을 할 때 가장 빠른 방법
"""

import timeit
import numpy

def while_loop(n=100_000_000):
    """
        흔한 while loop 구현의 경우 : 
        while loop 의 경우는 
            내부 increment (s += i, i += 1)
        모두 순수 파이썬으로 실행 됩니다. 
        따라서 매우 속도가 느립니다.
    """
    i = 0
    s = 0
    while(i < n):
        s += i
        i += 1

    return s

def for_loop(n=100_000_000):
    """
        흔한 for loop 구현의 경우 : 
        for loop 의 경우는 
            for i in range(n)
        실행이 내부 C 언어로 구현되어 있습니다.
        따라서 순수 파이썬으로 실행되는 while loop 보다 속도가 빠르게 됩니다.
    """
    s = 0 
    for i in range(n):
        s += i

    return s

def sum_range(n=100_000_000):
    """
        Built-In 함수인 sum() 을 활용하게 되면 
        위의 s += i 의 파이썬으로 실행되는 구문보다 
        빠르게 실행되므로 for loop 보다 더 빠르게 실행됩니다.
    """
    return sum(range(n))

def sum_numpy(n=100_000_000):
    """
        Numpy 같은 경우, 모든 연산을 C로 변환해 실행합니다.
        따라서 위 모든 경우 보다 빠르게 실행됩니다.
        참고로 numpy 는 해당 연산을 메모리에 캐싱하기 때문에 
        n 값이 너무 클 시 제한 될 수 있습니다.
    """
    return numpy.sum(numpy.arange(n))

def sum_math(n=100_000_000):
    """
        하지만 가장 빠른 방법은 역시 looping 자체를 하지 않는 방법이죠.
        수학을 잘해야 되는 이유...
    """
    return (n * n-1) // 2

if __name__ == '__main__':
    print("while loop \t\t", timeit.timeit(while_loop, number=1))
    print("for loop \t\t", timeit.timeit(for_loop, number=1))
    print("built-in sum loop \t\t", timeit.timeit(sum_range, number=1))
    print("numpy loop \t\t", timeit.timeit(sum_numpy, number=1))
    print("pure math \t\t", timeit.timeit(sum_math, number=1))

    """
        while loop 		 8.743821714000001
        for loop 		 5.6443756
        built-in sum loop 		 1.9486114690000012
        numpy loop 		 0.44622576599999775
        pure math 		 2.5380000003849545e-06
    """