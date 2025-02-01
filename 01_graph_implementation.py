def print_graph(graph):
    for node, neighbours in graph.items():
        print(f'{node}: {neighbours}')


if __name__ == "__main__":
    # edge list representation
    edge_list = [
        [1, 2], [2, 3], [3, 4], [4, 2], [1, 3]
    ]
    # adjacency list(undirected)
    graph = {}
    for a, b in edge_list:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    print_graph(graph)
