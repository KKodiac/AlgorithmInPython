def solution(): 
    def turn_left(d): 
        d = (d-1) % 4
        return d
    
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    
    # 조합으로 각각 북, 동, 남, 서
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    
    count = 1
    x, y = r, c
    matrix[x][y] = -1
    
    while True:
        check = False 
        for i in range(4): 
            d = turn_left(d)
            nx = x + dr[d]
            ny = y + dc[d]
            if 0 <= nx < n and 0 <= ny < m: 
                if matrix[nx][ny] == 0: 
                    count += 1
                    matrix[nx][ny] = -1 
                    x, y = nx, ny
                    check = True 
                    break
        if not check: 
            nx = x - dr[d]
            ny = y - dc[d]
            if 0 <= nx < n and 0 <= ny < m: 
                if matrix[nx][ny] == -1:
                    x, y = nx, ny
                elif matrix[nx][ny] == 1: 
                    print(count)
                    break
            else:
                print(count)
                break



if '__main__' == __name__:
    solution()