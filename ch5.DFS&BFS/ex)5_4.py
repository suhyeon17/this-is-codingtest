from collections import deque

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input())))

def short(board, r, c):
    queue = deque()

    #queue에 상하좌우 인접한 칸 중 괴물이 없는 칸 담기
    queue.append()
