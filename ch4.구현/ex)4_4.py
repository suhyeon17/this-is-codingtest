n, m = map(int, input().split())
row, col, dir = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

#이동했던 위치를 담기위한 2차원 리스트
visit = [[0]*m for _ in range(n)]
visit[row][col] = 1
#왼쪽으로 반시계 방향으로 바라보는 방향 90도 회전 -> 북, 서, 남, 동 순으로 회전함
turn_left = [0, 3, 2, 1]
#북, 서, 남, 동을 바라볼 때 각각의 왼쪽 방향 -> 서, 남, 동, 북
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
cnt = 1
dir_idx = turn_left.index(dir)
turn = 0

while True:
    #반시계 방향으로 4가지 방향 탐색
    for i in range(4):
        dir_idx += 1
        if dir_idx > 3:
            dir_idx = 0

        #바라보는 방향에서 왼쪽으로 이동
        nrow = row + moves[dir_idx][0]
        ncol = col + moves[dir_idx][1]

        if board[nrow][ncol] == 0 and visit[row][col] != 1:
            row, col = nrow, ncol
            visit[row][col] = 1
            cnt += 1
            turn = 0
            break
        else:
            turn += 1

    if turn == 4:
        break

print(cnt)



