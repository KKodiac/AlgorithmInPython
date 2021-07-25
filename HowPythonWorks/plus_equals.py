"""
    How += works extended
        augmented_operations.py
"""

class BadList(list):
    def __add__(self, other):
        """
            새로운 list 를 만들어 list.__add__ 를 호출 후
            BadList 로 변형
        """
        print("running custom add")
        return BadList(super(BadList, self).__add__(other))

    def __iadd__(self, other):
        """
            BadList.__add__(other) 을 호출
            -> 위의 정의 처럼 새로운 list 를 만듬
        """
        print("running custom iadd")
        return self + other

def plus_equals_pointers():
    """
        int 형은 immutable 이다
        파이썬에서는 변수가 가르키는 포인터를 변경 해주면서
        이것을 처리한다.

        아래 코드는 기존 x 가 1을 가르키고 있는 것을
        += 연산 이후 2로 가르키는 것을 바꾼것을 보여준다.
    """
    x = 1
    print(id(x))
    x += 1
    print(id(x), '바뀜')

    """
        리스트 같은 경우 포인터를 재할당 해주면서 
        용량이 큰 리스트일 경우 메모리를 많이 잡아 먹을 수 있다
        따라서 id(x) 값은 바뀌지 않는다.
    """
    x = []
    print(id(x))
    x += [1] 
    print(id(x), '안바뀜')

    """
        이러한 파이썬의 특징이 오류를 불러일으킬 수 있는 예시
        위 BadList 정의
            bad += [1,2,3] 이후 새로운 bad 가 생성된다.
        
    """
    bad = BadList()
    print(bad, "Append 전")
    bad += [1,2,3]
    append_to_bad(bad)
    print(bad, "Append 후")

def append_to_bad(l):
    """
        l += [4,5,6] 은 
        l.__iadd__([4,5,6]) 과 같음
        l 은 BadList 의 인스턴스이다. 따라서 
        BadList.__iadd__() 에 따라 새로운 l 이 생성되게 된다.
        하지만 l 은 함수 내 로컬 변수라 호출 이후 
        위 bad 에는 영향을 미치지 못한다.
    """
    l += [4,5,6]

def plus_equals_meaning():
    # x += y 
    result = x.i__iadd__(y)
    x = result

    # x[0] += y
    result = x[0].__iadd__(y)   # __getitem__ 호출
    x[0] = result               # __setitem__ 호출

    result = x.val.__iadd__(y)  # __getattr__ 호출
    x.val = result              # __setattr__ 호출

def main():
    plus_equals_pointers()

if __name__ == '__main__':
    main()

