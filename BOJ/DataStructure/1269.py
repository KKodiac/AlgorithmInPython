# BOJ 1269 대칭 차집합
def solution():
    len_a, len_b = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_b = set(a).difference(b)
    b_a = set(b).difference(a)
    print(len(a_b) + len(b_a))


if '__main__' == __name__:
    solution()