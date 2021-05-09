"""
    += Operation in Python
    How it works on mutables and immutables
"""

def tuple_what():
    # a_tuple = (1, 2)
    # a_tuple[0] += 1 # Error, tuple 은 immutable

    b_tuple = (["This is a list", "Lists are mutable"],
                ["This is a second element in list"])

    b_first_element = b_tuple[0]
    b_first_element += ["Added an element"] # List Type 이기 때문에 돌아감


    """
        출력 : 
        TypeError
        (['This is a list', 'Lists are mutable', 'Added an element', 'Adding to tuple index'], 
        ['This is a second element in list'])
    """

    try:
        b_tuple[0] += ["Adding to tuple index"] # Error
    except TypeError:
        print("TypeError")

    print(b_tuple) # Error 가 났는데도 첫 list의 마지막 요소에 추가한 요소가 반영됨
    

def plus_equals_meaning():
    # x += y 
    result = x.i__iadd__(y)
    x = result

    # x[0] += y
    result = x[0].__iadd__(y)   # __getitem__ 호출 -> x[0]에 y 요소 추가 성공
    x[0] = result               # __setitem__ 호출 -> x[0]에 immutable 요소이기 때문에 type error 오류

    result = x.val.__iadd__(y)  # __getattr__ 호출 -> x.val에 y 요소 추가 성공
    x.val = result              # __setattr__ 호출 -> 여기서 type error 오류

def main():
    tuple_what()

if __name__ == '__main__':
    main()
