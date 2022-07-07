from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n)]
for i in range(m):
    idx, city = map(int, input().split())
    graph[idx-1].append(city)


def findCity(graph, start, visited, cnt, short):
    queue = deque([start])
    visited[start - 1] = True

    while queue:  # queue가 빌 때까지
        v = queue.popleft()  # 큐에서 하나의 원소(방문한 원소) 뽑아서 출력

        for i in graph[v - 1]:
            if not visited[i - 1]:
                queue.append(i)
                visited[i - 1] = True
                if v != start:
                    cnt[i - 1] = 1 + cnt[v - 1]
                else:
                    cnt[i - 1] += 1
        print()
    answer = []
    for i in range(len(cnt)):
        if cnt[i] == short:
            answer.append(i + 1)

    return answer

city = [0] * n
visited = [False] * n

answer = findCity(graph, x, visited, city, k)

if len(answer) == 0:
    print('-1')
else:
    for i in range(len(answer)):
        print(answer[i])