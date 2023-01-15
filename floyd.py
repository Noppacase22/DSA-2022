from graph import Graph


def floyd(graph):
    n = len(graph.matrix)
    new_matrix = []

    for i in range(n):
        list = []
        for j in range(n):
            if graph.matrix[i][j] != 0:
                list.append(graph.matrix[i][j])
            else:
                list.append(float('inf'))
        new_matrix.append(list)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if new_matrix[j][k] > new_matrix[j][i] + new_matrix[i][k]:
                    new_matrix[j][k] = new_matrix[j][i] + new_matrix[i][k]
    
    for i in range(n):
        for j in range(n):
            if new_matrix[i][j] == float('inf') or i==j:
                new_matrix[i][j] = 0
    
    return new_matrix
    

if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 0, 9, 0], # 0
        [0, 0, 0, 0, 0, 0], # 1
        [0, 5, 0, 1, 0, 2], # 2
        [6, 0, 0, 0, 0, 2], # 3
        [0, 0, 0, 0, 0, 1], # 4
        [0, 6, 0, 0, 0, 0]  # 5   
    ]
    graph = Graph(matrix)
    D = floyd(graph)
    for i in range(6):
        for j in range(6):
            print(f"{D[i][j]:2d}", end=" ")
        print()
    #  0 12  7  8  9  9 
    #  0  0  0  0  0  0 
    #  7  5  0  1 16  2 
    #  6  8 13  0 15  2 
    #  0  7  0  0  0  1 
    #  0  6  0  0  0  0 