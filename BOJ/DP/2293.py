# BOJ 2293번 문제: 동전 1
# 전체 가능한 조합 세트의 종류는 두가지로 나뉜다
# i) 주어진 n 배열의 m 번째 값이 없는 경우
# ii) 주어진 n 배열의 m 번째 값이 있는 경우
def noDynamicProgramming(n, m, k):
    """DP 를 사용하지 않은 위 조건만 순수 부합하는 솔루션이다."""
    def count(n, m, k):
        if k == 0:
            """조합의 합이 k를 부합한 경우."""
            return 1
        elif k < 0:
            """조합의 합이 k를 넘어 부합하지 않는 경우."""
            return 0
        elif m <= 0 and k >= 0:
            """조합을 모두 더해도 k보다 작아 부합하지 않는 경우."""
            return 0
        else:
            """주어진 n 배열의 m번째 값이 조합에 포함 + 미포함 된 경우의 합."""
            return count(n, m-1, k) + count(n, m, k-n[m-1])

    answer = count(n, len(n), k)
    print(answer)


def DynamicProgramming(n, m, k):
    """중복된 연산이 있어 BottomUp 방식을 활용한 솔루션이다."""
    def count(n, m, k):
        table = [[0 for _ in range(m)] for __ in range(k+1)]

        # 조합의 합이 0 이어야 할 모든 경우의 값을 구해준다.
        for i in range(m):
            table[0][i] = 1

        # BottomUp 방식으로 나머지 table을 채워준다.
        # i 는 조합의 합을 의미한다.
        # j 는 조합 안의 값의 개수를 의미한다.
        for i in range(1, k+1):
            for j in range(m):
                include = table[i-n[j]][j] if i-n[j] >= 0 else 0
                exclude = table[i][j-1] if j >= 1 else 0

                table[i][j] = include + exclude

        return table[k][m-1]

    answer = count(n, m, k)
    print(answer)

if '__main__' == __name__:
    valueLen, valueSum = map(int, input().split())
    values = []
    for i in range(valueLen):
        values.append(int(input()))

    noDynamicProgramming(values, valueLen, valueSum)
    DynamicProgramming(values, valueLen, valueSum)

