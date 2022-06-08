# BOJ 10816 숫자카드2
from collections import Counter

def solution():
    n = int(input())
    hands = Counter(list(map(int, input().split())))
    m = int(input())
    cards_ = list(map(int, input().split()))
    cards = {c: 0 for c in cards_}

    for h in hands.keys():
        cards[h] = hands[h]

    print(" ".join(str(cards[card]) for card in cards_))



if '__main__' == __name__:
    solution()
