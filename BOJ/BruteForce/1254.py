# BOJ 1254 팰린드롬 만들기
def solution():
    s = list(str(input()))
    reverse_s = list(reversed(s))
    answer = len(s)
    for i in range(len(s)):

        if s[i:] == reverse_s[:len(s)-i]:
            answer += i
            break

    print(answer)

if '__main__' == __name__:
    solution()