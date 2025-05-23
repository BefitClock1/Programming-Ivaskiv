from collections import defaultdict, deque

def find_unreachable_cities(storages, cities, pipelines):
    graph = defaultdict(list)
    
    #граф
    for u, v in pipelines:
        graph[u].append(v)

    result = []

    # досяжність до міста для сховищз
    for storage in storages:
        visited = set()
        queue = deque([storage])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                queue.extend(graph[node])

        # міста які не були відвідані з цього сховища
        unreachable = [city for city in cities if city not in visited]
        if unreachable:
            result.append([storage, unreachable])

    return result
storages = ['Сховище_1', 'Сховище_2']
cities = ['Львів', 'Стрий', 'Долина', 'Поляна' ]
pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2'], ['Сховище_2', 'Долина']]

print(find_unreachable_cities(storages, cities, pipelines))
#  [['Сховище_1', ['Львів', 'Стрий']]]
