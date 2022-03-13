# Programmers BFS-DFS problem: Target Number
def solution(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-1*numbers[0], 0]]
    n = len(numbers)
    while stack:
        temp, idx = stack.pop()
        idx += 1
        if idx < n:
            stack.append([temp+numbers[idx], idx])
            stack.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1

    return answer


if '__main__' == __name__:
    print(solution([1,1,1,1,1], 3))



