from graph import Graph

class EDGE:
    def __init__(self, u, v, weight):
        self.node1 = u
        self.node2 = v
        self.weight = weight
        

def find_set(current_set, vertex):
    for i in range(len(current_set)):
        if vertex in current_set[i]: return i
    return -1

def kruskal(graph):
    n = len(graph.matrix)
    current_sets = [[0]]
    edge_list = []
    for i in range(1,n):
        current_sets.append([i])
        for j in range(i):
            a = graph.matrix[i][j]
            if a == 0: a = float("inf")
            edge = EDGE(i, j, a)
            edge_list.append(edge)
    edge_list.sort(key=lambda x: x.weight)

    final_list = []
    for edge in edge_list:
        a = find_set(current_sets, edge.node1)
        b = find_set(current_sets, edge.node2)
        if a != b:
            final_list.append(edge)
            for item in current_sets[b]:
                current_sets[a].append(item)
            current_sets.pop(b)

    new_graph = []
    for i in range(n):
        new_graph.append([0]*n)
    for edge in final_list:
        new_graph[edge.node1][edge.node2] = edge.weight
        new_graph[edge.node2][edge.node1] = edge.weight
    return Graph(new_graph)
    
 
if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 6, 9, 0], # 0
        [0, 0, 5, 0, 0, 6], # 1
        [7, 5, 0, 1, 0, 2], # 2
        [6, 0, 1, 0, 0, 2], # 3
        [9, 0, 0, 0, 0, 1], # 4
        [0, 6, 2, 2, 1, 0]  # 5    
    ]
    graph = Graph(matrix)
    graph.bf_print(0)   # 0 2 3 4 1 5
    mst = kruskal(graph)
    mst.bf_print(0)     # 0 3 2 1 5 4