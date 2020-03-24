from math import inf
import random
import numpy as np

# Defining an undirected graph network with connectivity matrix as attributes
class SymMatrix:
    # Initializer/Constructor matrix
    def __init__(self, size):
        if size <= 0:
            raise ValueError("size has to be positive value")

        self.size = size
        self.data = [0 for i in range((size + 1) * size // 2)]
        self.matrix = np.zeros((size,size))

    # Specificifng the symmetric network nodes (e.g. 6 nodes == 6x6 connectivity matrix)
    def __len__(self):
        return (self.size*self.size)

    # Writing/set items in the matrix
    def __setitem__(self, position, value):
        index = self.get_index(position)
        self.data[index] = value
        self.matrix = self.get_matrix()

    # Reading set items in the matrix
    def __getitem__(self, position):
        # index = self.get_index(position)

        # return self.data[index], self.data, self.matrix

        # Returning graph matrix
        return self.matrix

    def get_matrix(self):
        indices = np.tril_indices(self.size)
        self.matrix[indices] = self.data

        return self.matrix

    # Calculating the index
    def get_index(self, position):
        row, col = position
        if col > row:
            row, col = col, row 
        index = (0 + row) * (row + 1) // 2 + col

        return index