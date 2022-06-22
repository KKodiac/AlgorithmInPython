from itertools import combinations

def solution():
    height = []
    for _ in range(9):
        height.append(int(input()))

    for combination in list(combinations(height, r=7)):
        if sum(combination) == 100:
            for i in sorted(list(combination)):
                print(i)
            break

if '__main__' == __name__:
    solution()