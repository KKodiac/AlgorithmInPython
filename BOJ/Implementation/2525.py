# BOJ 2525번 문제: 오븐 시계
def solution():
    A, B = map(int, input().split())
    C = int(input())

    hours = C // 60
    minutes = C % 60

    A += hours
    B += minutes

    if A > 23:
        A -= 24
    if B > 59:
        B -= 60
        A += 1

    if A > 23:
        A -= 24

    print(A, B, sep=" ")

if '__main__' == __name__:
    solution()

