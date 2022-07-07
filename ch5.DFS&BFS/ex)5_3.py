n, m = map(int, input().split())

tray = []
for i in range(n):
    tray.append(list(map(int, input())))

def makeIce(tray, r, c):
    #재귀 종료 조건
    if r < 0 or r >= n or c < 0 or c >= m:
        return 0

    if tray[r][c] == 0:
        tray[r][c] = 1 #방문처리

        makeIce(tray, r-1, c)  # 상
        makeIce(tray, r+1, c)  # 하
        makeIce(tray, r, c-1)  # 좌
        makeIce(tray, r, c+1)  # 우

        return 1

    return 0

ice = 0
for i in range(n):
    for j in range(m):
        ice += makeIce(tray, i, j)

print(ice)