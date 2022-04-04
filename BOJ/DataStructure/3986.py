# BOJ 3986 번 문제 : 좋은 단어
from sys import stdin
def solution():
    N = int(input())
    good_word_count = 0
    for _ in range(N):
        words = stdin.readline().strip()
        # if len(words) % 2:
        #     continue
        
        stack = list()
        for letter in words:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
            
        if not stack:
            good_word_count += 1
    print(good_word_count)

if '__main__' == __name__:
    solution()