def solution():
    x = int(input())
    row = 0
    idx = 0
    for i in range(1, x+1):
        row += i
        if row >= x:
            idx = i
            break

    inc = x - (row - idx) - 1
    if idx % 2 == 0:
        y_ = (idx - 1) - inc
        x_ = inc
    else:
        x_ = (idx - 1) - inc
        y_ = inc

    print(f"{x_+1}/{y_+1}")


if '__main__' == __name__:
    solution()