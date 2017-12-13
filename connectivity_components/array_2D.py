def f(data, start, visited, graph=None):
    if data and start:
        x, y = start[0], start[1]
        if  graph is None:
            graph = [start]
            visited.append(start)
        for a, b in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if [a, b] in data and [a, b] not in visited:
                graph.append([a, b])
                visited.append([a, b])
                f(data, [a, b], visited, graph)
    return graph, visited


if __name__ == '__main__':
    connect_comp = []
    visited = []
    data = [[0, 0], [0, 1], [1, 1], [2, 1], [3, 1], [3, 0], [5, 5], [4, 5], [6, 5]]
    for vertex in data:
        if vertex not in visited:
            result = f(data, vertex, visited)
            visited = result[1]
            connect_comp.append(result[0])
            print(result[0])
    print('Число компонент связности:\n', len(connect_comp))
