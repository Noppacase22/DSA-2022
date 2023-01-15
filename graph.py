class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        return None

    def _print(self, start: int, mode):
        seen_nodes = set()
        node_stack = [start]
        matrix = self.matrix
        while (len(node_stack) > 0):
            if mode == "df": current_node = node_stack.pop()
            else: current_node = node_stack.pop(0)
            if current_node in seen_nodes: continue

            print(current_node, end=" ")
            seen_nodes.add(current_node)
            current_list = []
            for i in range(len(matrix)):
                if matrix[current_node][i] != 0 and i not in seen_nodes:
                    current_list.append(i)
            if mode == "df":
                current_list.reverse()
            for node in current_list: node_stack.append(node)
        print()
        return None

    
    def df_print(self, start: int):
        self._print(start, "df")
        return None
    
    def bf_print(self, start: int):
        self._print(start, "bf")
        return None
    
    def weight(self, vertex1: int, vertex2: int):
        length = self.matrix[vertex1][vertex2]
        if length != 0: return length
        return -1

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
    graph.df_print(0)           # 0 2 1 3 5 4 
    graph.bf_print(0)           # 0 2 4 1 3 5 
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1
    print()
    # Codegrade test case 2
    new = [
        [0, 5, 3, 6, 0, 6],     # 0 1 3 5 2 4 
        [0, 0, 0, 6, 0, 2],     # 1 3 5
        [0, 1, 0, 3, 3, 4],     # 2 1 3 5 4 0
        [0, 0, 0, 0, 0, 1],     # 3 5
        [2, 2, 0, 3, 0, 4],     # 4 0 1 3 5 2
        [0, 0, 0, 0, 0, 0]      # 5
    ]
    new_graph = Graph(new)
    for i in range(6):
        new_graph.df_print(i)