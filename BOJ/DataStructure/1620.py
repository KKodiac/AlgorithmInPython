# BOJ 1620 나는야 포켓몬 마스터 이다솜
import sys


def solution():
    n, m = map(int, input().split())
    pokedex_by_str = {}
    pokedex_by_int = []
    for i in range(1, n+1):
        pokemon = sys.stdin.readline().rstrip()
        pokedex_by_str[pokemon] = i
        pokedex_by_int.append(pokemon)

    for _ in range(m):
        name_or_index = sys.stdin.readline().rstrip()
        if 48 <= ord(name_or_index[0]) <= 57:
            name_or_index = int(name_or_index)
            print(pokedex_by_int[name_or_index-1])
        else:
            name_or_index = str(name_or_index)
            print(pokedex_by_str[name_or_index])


if '__main__' == __name__:
    solution()
    