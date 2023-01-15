
from graph import Graph

def dijkstragraph(graph: Graph, start: int):
    matrix = graph.matrix
    n = len(matrix)
    distances = []
    parents = [0]*n
    unused_verticies = []
    for i in range(n):
        distances.append(0)
        unused_verticies.append(i)
        if distances[i] == 0 and i != start: distances[i] = float("inf")
    current_node = start    # index

    while len(unused_verticies) > 0:
        unused_verticies.remove(current_node)        
        for i in range(n):
            node_to_i = matrix[current_node][i]
            if node_to_i != 0 and (distances[current_node] + node_to_i < distances[i]):
                distances[i] = distances[current_node] + node_to_i
                parents[i] = current_node
        
        if len(unused_verticies) == 0:
            break
        
        min = unused_verticies[0]
        for index in unused_verticies:
            if distances[index] < distances[min]:
                min = index
        current_node = min     

    new_graph = []
    for i in range(n):
        list = []
        for j in range(n):
            list.append(0)
        new_graph.append(list)
    for i in range(n):
        new_graph[parents[i]][i] = graph.matrix[parents[i]][i]
        
    return Graph(new_graph)


if __name__ == "__main__":

    matrix = [
        [0, 25,  6,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, 10,  3,  0,  0,  0,  0,  0],
        [0,  0,  0,  7,  0, 25,  0,  0,  0,  0],
        [0,  0,  0,  0, 12, 15,  4, 15, 20,  0],
        [0,  0,  0,  0,  0,  0,  0,  2,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  2,  0],
        [0,  0,  0,  0,  0,  0,  0,  8, 13, 15],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  5],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        ]

    graph = Graph(matrix)

    new_graph = dijkstragraph(graph, 0)
    new_graph.df_print(0)           # 0 1 2 3 4 5 6 7 9 8 
    new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    print(new_graph.weight(3, 6))   # 4
    print(new_graph.weight(5, 8))   # -1