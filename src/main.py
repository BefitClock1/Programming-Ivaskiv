from collections import defaultdict, deque
import csv
# read_file('map.csv')

def read_file(filename):
    with open(filename, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        lines = list(reader)
    
    farms = lines[0]
    shops = lines[1]
    roads = lines[2:]

    # print("Farms:", farms)
    # print("Shops:", shops)
    # print("Roads:")
    # for road in roads:
    #     print(road)
    return farms, shops, roads

def build_graph(farms, shops, roads):
    graph = defaultdict(dict)

    for road in roads:
        u, v, capacity = road
        graph[u][v] = int(capacity)
    
    super_source = 'SRC'
    super_sink = 'SNK'

    for farm in farms:
        graph[super_source][farm] = float('inf')
    for shop in shops:
        graph[shop][super_sink] = float('inf')
    
    return graph, super_source, super_sink

def bfs(graph, src, sink, parent):
    visited = set()
    queue = deque([src])
    visited.add(src)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
                visited.add(v)
    return False

def edmonds_karp(graph, source, sink):
    max_flow = 0

    while True:
        parent = {}  
        if not bfs(graph, source, sink, parent):
            break

        # знайти мінімальний потік уздовж шляху
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # оновити залишковий граф
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v].setdefault(u, 0)  # якщо зворотної ребра ще не було
            graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

graph, src, sink = build_graph(*read_file('map.csv'))
flow = edmonds_karp(graph, src, sink)
print("Максимальна кількість машин:", flow)
