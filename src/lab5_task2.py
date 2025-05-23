# Переписаний код із використанням графів
def graph(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False] * m for _ in range(n)]
    graphs = []

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def dfs(i, j, current_graph):
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            if not visited[x][y]:
                visited[x][y] = True
                current_graph.add((x, y))
                for dx, dy in directions:
                    ni, nj = x + dx, y + dy
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] >= 1 and not visited[ni][nj]:
                        stack.append((ni, nj))

    for i in range(n):
        for j in range(m):
            if matrix[i][j] >= 1 and not visited[i][j]:
                current_graph = set()
                dfs(i, j, current_graph)
                graphs.append(current_graph)

    return graphs

matrix = [
    [1, 1, 1, 0, 0, 2],
    [1, 1, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 3, 3, 3, 0],
]

graphs = graph(matrix)
print(f"Кількість островів: {len(graphs)}")
for g in graphs:
    print(g)
