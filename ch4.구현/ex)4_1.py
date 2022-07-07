n = int(input())
dirs = input().split()

#L, R, U, D 움직일 수 있는 방향 벡터 정의
dx = [0, 0, -1, 1] #U가 위로 올라가는거이므로 -!
dy = [-1, 1, 0, 0] #L이 왼쪽이므로 -1

#시작좌표
x = 1
y = 1

#입력받은 방향대로 움직이기 -> 새로운 방향 = 기존 + dx/dy
for dir in dirs:
    if dir == 'L':
        i = 0
    elif dir == 'R':
        i = 1
    elif dir == 'U':
        i = 2
    else:
        i = 3

    nx = x + dx[i]
    ny = y + dy[i]

    #NXN 내에서만 이동하도록
    if nx >= 1 and nx <= 5 and ny >= 1 and ny <= 5:
        x, y = nx, ny

print(x, y)


