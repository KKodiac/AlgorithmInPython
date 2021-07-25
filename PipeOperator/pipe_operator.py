import random
import time
"""
Dictionary Union, also know as Pipe Operator ( | )
데이타타입1 | 데이타타입2 => 두 데이터타입이 연결된 값을 반환합니다.
파이썬 3.9 부터 딕셔너리 타입도 가능하게 되었습니다.
"""

"""
해당 두 가지 명령문은 같은 결과를 반환합니다.
리스트 같은 경우는 + 연산자가 되기 때문에 상관 없지만,
셋은 + 연산자를 사용할 시, TypeError 가 뜹니다. (딕셔너리도 같음)
따라서 | 연산자(pipe operator) 을 활용하면 두 타입을 연결할 수 있습니다.
"""
def test_combining_list_set():
    a = [1,2,3]
    b = [4]

    assert a + b == [1,2,3,4] # Passes

    c = {1,2,3}
    d = {4}
    assert c | d == {1,2,3,4} # Passes

"""
딕셔너리 연산을 기존 변수를 변경하지 않고 새 값을 반환하여 줍니다.
"""
def test_dict_or_disjoint_keys():
    a = {'key1' : 1, 'key2' : 2, 'key3' : 3}
    b = {'key4' : 4}

    assert a | b == {'key1' : 1, 'key2' : 2, 'key3' : 3, 'key4' : 4} # Passes
    assert a == {'key1' : 1, 'key2' : 2, 'key3' : 3}                 # Passes
    assert b == {'key4' : 4}                                         # Passes


"""
중복되는 키 값이 있다면 가장 최근에 찾은 값으로 대체 합니다.
아래 예시 같은 경우는 가장 최근 찾은 값(5) 를 해당 키에 값으로 대입합니다.
"""
def test_dict_or_non_disjoint_keys():
    a = {'key1' : 1, 'key2' : 2, 'key3' : 3}
    b = {'key3' : 5, 'key4' : 6}

    assert a | b == {'key1' : 1, 'key2' : 2, 'key3' : 5, 'key4' : 6} # Passes, Latest found 'key3' value : 5
    assert b | a == {'key1' : 1, 'key2' : 2, 'key3' : 3, 'key4' : 6} # Passes, Latest found 'key3' value : 3
    assert a | b != b | a                                            # Passes

"""
True 와 1 은 파이썬에서 다른 타입 (Boolean and Int) 이기 때문에 비교 시 거짓이 뜬다
"""
def test_true_and_integer_type():
    a = True
    b = 1

    assert a is not b    # Passes
    assert a or b is a   # Passes, 파이썬은 or 연산 시 참을 반환 하게 되는 시점의 변수를 반환합니다. a 비교 시 참이 떴으므로 a 를 반환합니다.
    assert b or a is b   # Passes, 위와 동일 합니다.

"""
Pipe Operator 은 사칙연산자 등 과 같이 |= 문법을 사용할 수 있다.
"""
def test_dict_ior_syntax():
    a = {'key1' : 1, 'key2' : 2, 'key3' : 3}
    b = {'key4' : 4}

    a |= b               # a.update(b) 와 같다.

    assert a == {'key1' : 1, 'key2' : 2, 'key3' : 3, 'key4' : 4} # Passes

    # syntax error
    # assert (a |= b) == {'key1' : 1, 'key2' : 2, 'key3' : 3, 'key4' : 4}
    # 해당 연산은 +=, -= 등과 같이 값을 반환하지 않는다. 단지 a 를 업데이트 해줄 뿐이다.

"""
Pipe Operator 을 연쇄적으로 사용 가능하다.
d = a + b + c 같은 연산은 연산 사이사이에 임시 변수를 생성하는데, 이것은 퍼포먼스에 지장을 줄 수 있다.
Pipe Operator 을 연쇄적으로 활용한 것과 임시 변수 생성 없이 for 문으로 한 것을 비교해보자.
"""
def test_time_dict_aggregation():
    M = 10000000
    size = 1000000
    a = {x: random.randint(0,M) for x in range(size)}
    b = {x: random.randint(0,M) for x in range(size)}
    c = {x: random.randint(0,M) for x in range(size)}
    d = {x: random.randint(0,M) for x in range(size)}

    # Operator Chaining
    start = time.perf_counter()
    e = a | b | c | d
    elapsed1 = time.perf_counter() - start
    print(f"Operator Chaining : {elapsed1}")

    # Without operator chaining, 임시 변수 없음
    start = time.perf_counter()
    for option in [a,b,c,d]:
        e |= option
    elapsed2 = time.perf_counter() - start
    print(f"Without Operator Chaining : {elapsed2}")







