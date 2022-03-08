# BOJ 13305번 문제: 주유소
def solution():
    N = int(input())
    road = list(map(int, input().split()))
    liter = list(map(int, input().split()))
    liter.pop()

    minimum_liter = liter[0]
    total_cost = road[0] * minimum_liter

    for i in range(1, N-1):
        if liter[i] < minimum_liter:
            minimum_liter = liter[i]
        total_cost += road[i] * minimum_liter

    print(total_cost)
    



if '__main__' == __name__:
    solution()
