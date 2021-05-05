"""
    함수가 정의 되고 있을 때 정의 시 호출 한 다른 함수가 실행 됩니다.
    따라서 함수의 인자로 지정된 변수들은 함수 정의 시에 매모리에 생성이 됩니다.
"""

def do_something(opt: print("This runs"), arg=print("This also runs")) -> 3:
    pass

"""
    위 조건에 따라서 arg=[] 의 
    arg 이라는 변수는 함수 정의 시 생성이 되기 때문에 이후 액세스 할 때도 공유됩니다.
"""
def do_something_another(arg=[]):
    print(arg)
    arg.append(0)
    

if __name__ == '__main__':
    do_something(0)
    print(do_something.__annotations__) # 함수 인자와 인자 기본 타입을 출력 {'opt: None', 'return': 3}
    
    print(do_something_another.__defaults__)    # 함수 인자의 기본 값을 출력 ([],)
    do_something_another()  # prints []
    do_something_another()  # prints [0]
    print(do_something_another.__defaults__)    # 함수 인자의 기본 값을 출력 ([0,0],)
