# 최대공약수 -> 유클리드 호제법
# a 를 b 로 나눈 나머지로 b 를 계속 나눈다.
# b는갱신된 나머지 값으로 대체한다.
# 최소공배수 -> 기존 값의 곱 // 최대공약수
def main():
    num1, num2 = map(int, input().split())
    a = num1
    b = num2
    if a < b:
        a, b = b, a
    while a % b:
        ta = a % b
        a = b
        b = ta
    gcd = b
    lcm = (num1 * num2) // gcd
    print(gcd)
    print(lcm)





if __name__ == '__main__':
    main()
