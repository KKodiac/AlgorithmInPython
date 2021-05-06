"""
    WITHOUT
    Class 내의 파이썬 built-in 메서드 없이 사용해보자.
"""

class IntsAndSum:
    def __init__(self, ints: list[int], precomputed_sum: int = None):
        self.ints : list[int] = ints
        self.sum : int = precomputed_sum if precomputed_sum is not None else sum(ints)

    """
        __repr__ : 출력될 수 있는 표현을 문자열 형태로 반환
        __str__: 객체의 문자열 형태를 반환
    """
    def __repr__(self):
        return f'{self.__class__.__name__}({self.ints}, sum={self.sum})\n'

    """

    """
    @staticmethod
    def max(*args):
        return max(args, key=lambda x : x.sum)

    def append(self, i: int) -> None:
        self.ints.append(i)
        self.sum += i

    def copy(self):
        return IntsAndSum(ints=self.ints.copy(), precomputed_sum=self.sum)


def main():
    ias = [
        IntsAndSum([1, 6, 1]), 
        IntsAndSum([2, 5, 1, 1, 0]), 
        IntsAndSum([0, 1, 0])
    ]

    print(ias)
    # 인스턴스의 메서드로 max를 만들어줌
    print(IntsAndSum.max(*ias))

if __name__ == '__main__':
    main()