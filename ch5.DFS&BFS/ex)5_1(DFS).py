def dfs(graph, v, visited):
    visited[v] = True #방문 처리
    print(v)

    for i in graph[v]: #현재 노드와 연결된 다른 노드 방문
        if not visited[v]:
            dfs(graph, i, visited)
