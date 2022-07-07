from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #현재 노드 방문처리

    while queue: #queue가 빌 때까지
        v = queue.popleft() #큐에서 하나의 원소(방문한 원소) 뽑아서 출력
        print(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
