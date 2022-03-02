from collections import deque
import sys

def main():
"""
처음 풀이로 시간 초과
while + for 문으로 인해 O(n^2)

    N  = int(input())
    q  = deque(list(map(int, sys.stdin.readline().split())))
    nges = list()
    
    while len(q):
        A = q.popleft()
        found = False
        

        for i in q:
            if i > A:
                nges.append(i)
                found = True
                break
        if not found:
            nges.append(-1)
        
    print(" ".join(str(i) for i in nges))
"""

"""
    정담 풀이:
    A[i] 의 값 보다 작은 값의 인덱스를 저장하는 stack 변수를 활용한다
    만약 A[i] 이 기존 stack 에 저장 된 인덱스들에 해당하는 값보다 크다면
    여태 저장된 stack 내 인덱스들에 해당하는 값들의 인덱스를 활용하여 result[해당하는 값들의 인덱스] 에 A[i](가장 큰 가까운 값)을
    저장한다.
    만약 해당 값의 인덱스가 없다면 -1을 출력한다
"""

    N = int(input())
    A = list(map(int, sys.stdin.readline().split()))

    stack = []
    result = [-1 for i in range(N)]

    for i in range(N):
        while len(stack) and A[stack[-1]] < A[i]:
            result[stack.pop()] = A[i]
        stack.append(i)
    
    print(*result)
if __name__ == '__main__':
    main()