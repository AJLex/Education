def f(data, start, graph=None):
    if data and start:
        x, y = start[0], start[1]
        if  graph is None:
            graph = [start]
            data.remove(start)
        if [x+1, y] in data:
            graph.append([x+1, y])
            data.remove([x+1, y])
            f(data, [x+1, y], graph)
        if [x, y+1] in data:
            graph.append([x, y+1])
            data.remove([x, y+1])
            f(data, [x, y+1], graph)
        if [x-1, y] in data:
            graph.append([x-1, y])
            data.remove([x-1, y])
            f(data, [x-1, y], graph)
        if [x, y-1] in data:
            graph.append([x, y-1])
            data.remove([x, y-1])
            f(data, [x, y-1], graph)
    return data, graph


if __name__ == '__main__':
    connect_comp = []
    data = [[0, 0], [0, 1], [1, 1], [2, 1], [3, 1], [3, 0], [5, 5], [4, 5], [6, 5]]
    for vertex in data:
        result = f(data, vertex)
        data = result[0]
        connect_comp.append(result[1])
    print('Число компонент связности:\n', len(connect_comp))
