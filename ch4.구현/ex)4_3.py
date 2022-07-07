now = input()

#ord('a') = 97
row = (ord(now[0]) - 96)
col = int(now[1])
#움직일 수 있는 방향 정의
dirs = [(2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (1, -2), (-1, 2), (1, 2)]

cnt = 0
#현재 위치에서 방향에 맞게 움직이기
for dir in dirs:
    nrow = row + dir[0]
    ncol = col + dir[1]

    #정원을 벗어나지 않으면 카운트
    if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
        cnt += 1

print(cnt)