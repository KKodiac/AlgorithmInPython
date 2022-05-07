def solution():
    N = str(input())
    table = [0] * 10
    for n in N:
        table[int(n)] += 1
    answer = reversed([str(c)*i for c, i in enumerate(table)])
    print("".join(j for j in answer))

if '__main__' == __name__:
    solution()