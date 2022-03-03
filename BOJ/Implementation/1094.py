# 백준 1094번: 막대기
def solution():
    X = int(input())
    stick = 64
    stick_bag = [64]
    while sum(stick_bag) > X:
        smallest_stick = stick_bag.pop(stick_bag.index(min(stick_bag)))
        stick_bag.append(smallest_stick / 2)
        if sum(stick_bag) < X:
            stick_bag.append(smallest_stick / 2)
    
    print(len(stick_bag))
        
if '__main__' == __name__:
    solution()

