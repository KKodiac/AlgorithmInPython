"""
    비어있고 참인 데이타 타입은 파이썬에서 존재하나?

"""

def check_empty_truthy(x):
    """ If 문에 들어가면 참, for 문이 돌아가지 않으면 비어있음"""
    if x:
        print("참이다")
    
    for item in x:
        print("비어 있지 않다")


if __name__ == '__main__':
    gen = (_ for _ in [])

    check_empty_truthy({})
    check_empty_truthy([])
    check_empty_truthy(tuple())

    # generator 같은 경우가 조건에 성립하는 것을 볼 수 있다.
    check_empty_truthy(gen)