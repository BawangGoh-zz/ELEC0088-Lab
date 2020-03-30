import numpy as np
import string

# Graph Visualization libraries
import networkx as nx
import matplotlib.pyplot as plt

# Defining an undirected graph network with connectivity matrix as attributes
class SymMatrix:
    # Initializer/Constructor matrix
    def __init__(self, size):
        if size <= 0:
            raise ValueError("size has to be positive value")

        self._size = size
        self._data = [0 for i in range((size + 1) * size // 2)]
        self._matrix = np.zeros((size,size))

    # Specificifng the symmetric network nodes (e.g. 6 nodes == 6x6 connectivity matrix)
    def __len__(self):
        return (self._size*self._size)

    # Writing/set items in the matrix
    def __setitem__(self, position, value):
        index = self._get_index(position)
        self._data[index] = value
        self._matrix = self._get_matrix()

    # Reading set items in the matrix
    def __getitem__(self):
        # Returning graph matrix
        return self._matrix

    def _get_matrix(self):
        indices = np.tril_indices(self._size)
        self._matrix[indices] = self._data
        self._matrix = self._matrix.T

        return self._matrix

    # Calculating the index
    def _get_index(self, position):
        row, col = position
        index = (0 + row) * (row + 1) // 2 + col

        return index


# Define a class for visualizing the graph and return the shortest path
class VisualGraph(SymMatrix):
    def __init__(self, size):
        super().__init__(size)

    # Use the adjacent matrix earlier to draw edges of graph
    def _draw_graph(self, _matrix):
        # Create graph
        G = nx.from_numpy_matrix(_matrix)
        graph_layout = nx.spring_layout(G)
        node_lab = dict(zip(G.nodes, string.ascii_lowercase))
        edge_lab = nx.get_edge_attributes(G, "weight")

        # Draw Graph
        nx.draw_networkx(G, pos=graph_layout, labels=node_lab)
        nx.draw_networkx_edge_labels(G, pos=graph_layout, edge_labels=edge_lab)
        # plt.show()

    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
          
        # from the dist array,pick one which has min value and is still in queue 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 

        return min_index

    # Function to print shortest path from source to j using parent array 
    def printPath(self, parent, j): 
        #Base Case : If j is source 
        if parent[j] == -1 :  
            print(j, end='')
            return
        self.printPath(parent , parent[j]) 
        print(j, end='')

    def printSolution(self, dist, parent): 
        src = 0
        print("Vertex \tDistance from Source\tPath") 
        for i in range(1, len(dist)): 
            print("\n%d --> %d \t%d \t\t" % (src, i, dist[i]), end='') 
            self.printPath(parent,i) 

    def _dijkstra(self, graph, src): 
        row = len(graph) 
        col = len(graph[1]) 
  
        # The output array. dist[i] will hold the shortest distance from src to i 
        # Initialize all distances as INFINITE  
        dist = [float("Inf")] * row 
  
        # Parent array to store shortest path tree 
        parent = [-1] * row 
        
        # Distance of source vertex from itself is always 0 
        dist[src] = 0

        # Add all vertices in queue 
        queue = [] 
        for i in range(row): 
            queue.append(i) 

        #Find shortest path for all vertices 
        while queue: 
            # Pick the minimum dist vertex from the set of vertices still in queue 
            u = self.minDistance(dist,queue)  
  
            # remove min element      
            queue.remove(u) 
  
            # Update dist value and parent index of the adjacent vertices of the picked vertex. 
            # Consider only those vertices which are still in queue 
            for i in range(col): 
                '''Update dist[i] only if it is in queue, there is an edge from u to i, and total weight of path from 
                src to i through u is smaller than current value of dist[i]'''
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 

        # print the constructed distance array 
        self.printSolution(dist,parent) 