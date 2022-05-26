# BOJ 10799번 문제: 쇠막대기
def solution():
    pipe = str(input())

    stack = list()
    answer = 0
    for p in pipe:
        if p == '(':
            stack.append(p)
        else:
            ele = stack.pop()
            if ele == '(':
                answer += len(stack)
            else:
                answer += 1

    print(answer)
                

if '__main__' == __name__:
    solution()
            

