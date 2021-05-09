"""
    Following example shows why we don't assign variables 
    in a global scope. (Or at least avoid such action and surround it with local scope)
"""

def f():
    """
        *** NameError ***
        전역/로컬에 x 가 정의 안되어 있음을 감지
    """
    print(x)

def g():
    """
        *** UnboundLocalError ***
        Local Scope 에 x의 정의가 있음을 감지
    """
    print(x)
    x = 1

y = 0

def h():
    """ 
        prints 0 
    """
    print(y)

def j():
    """ 
        *** UnboundLocalError ***

        위에 y변수가 전역변수로 지정이 되어 있음애도 
        해당 함수의 로컬변수로 y 가 정의가 되어 있어서
        y 를 로컬변수로 판단하여 위 exception을 일으킴 
    """
    print(y)
    y = 1

def main():
    x = 1 # 각 함수에 영향 없음, 로컬 변수
    f()
    g()
    h()
    j()

"""
    이 안에 변수를 정의하면 전역변수로 판단 되어 j() 와 같은
    상황이 나올 수 있음

    따라서 위 main() 처럼 함수 내에 로컬 스콥으로 정의를 한 후에
    if __name__ == '__main__' 에서 실행하는 것이 바람직
"""
if __name__ == '__main__':
    # x = 2
    main()