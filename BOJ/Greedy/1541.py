# BOJ 1541번 문제: 잃어버린 괄호
def solution():
    equation = str(input())
    parenthesis = equation.split('-')
    parenthesis = [list(map(int, i.split('+'))) for i in parenthesis]

    answer = sum(parenthesis[0])
    for p in parenthesis[1:]:
        answer -= sum(p)

    print(answer)


if '__main__' == __name__:
    solution()
