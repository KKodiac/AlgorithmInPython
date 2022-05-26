def solution():
    class Board:
        def __init__(self, size):
            self.N = size
            self.queens = []
            self.answer = 0

        def is_queen_safe(self, row, col):
            for r, c in enumerate(self.queens):
                if r == row or c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def solve(self):
            self.queens = []
            col = row = 0
            while True:
                while col < self.N and not self.is_queen_safe(row, col):
                    col += 1
                if col < self.N:
                    self.queens.append(col)
                    if row + 1 >= self.N:
                        self.answer += 1
                        self.queens.pop()
                        col = self.N
                    else:
                        row += 1
                        col = 0
                if col >= self.N:
                    # 해당 row 에 퀸들 못 놓는경우
                    if row == 0:
                        return  # all combinations were tried
                    col = self.queens.pop() + 1
                    row -= 1
    n = int(input())
    q = Board(n)
    q.solve()
    print(q.answer)


if '__main__' == __name__:
    solution()