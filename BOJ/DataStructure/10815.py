# BOJ 10815 숫자카드
def solution():
    n = int(input())
    hands = list(map(int, input().split()))
    m = int(input())
    cards = {c: 0 for c in map(int, input().split())}

    for h in hands:
        cards[h] = 1

    print(" ".join(str(i) for i in list(cards.values())[:m]))


if '__main__' == __name__:
    solution()
