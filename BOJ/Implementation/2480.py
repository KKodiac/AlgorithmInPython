# BOJ 2480번 문제: 주사위 세개
def solution():
    dice_role = list(map(int, input().split()))

    price_role = 0      # 같은 눈의 수
    role_value = 0      # 다이스 눈의 값
    for i in dice_role:
        if dice_role.count(i) > price_role:
            price_role = dice_role.count(i)
            role_value = i

    price = 0
    if price_role == 1:
        price = max(dice_role) * 100
    elif price_role == 2:
        price = 1000 + role_value * 100
    elif price_role == 3:
        price = 10000 + role_value * 1000

    print(price)

if '__main__' == __name__:
    solution()
