from math import inf
import random
import numpy as np

# Defining an undirected graph network with connectivity matrix as attributes
# Input the lower triangular element of the matrix
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
    def __setitem__(self, value=[]):
        self.data = value
        self.matrix = self.get_matrix()

    # Reading set items in the matrix
    def __getitem__(self, data, matrix):
        return self.data, self.matrix

    def get_matrix(self):
        indices = np.tril_indices(self.size)
        self.matrix[indices] = self.data

        return self.matrix