## Part 1) Define a class network with a connectivity matrix of the nodes as an attribute and a method 
## that calculates the shortest path between two given nodes using the Dijkstra algorithm. 
## It should return the list of nodes of the path. One suggestion on how to store the connectivity 
## matrix is to use nested lists.

## Part 2) Deﬁne a subclass of network called tree. A tree is a network without any possibility for loops. 
## It should have a new attribute root and a method depth that calculates the depth of the tree. This method 
## can use the shortest path method.

from ManualSymMatrix import SymMatrix
from math import inf

def main():
    # Networks with 6 nodes
    sm = SymMatrix(6)

    # Input element into list to convert to graph matrix
    '''
    i - indicate infinite
        0 1 2 3 4 5 
    0   0 2 5 i 1 i ---------> 0
    1   2 0 3 2 i i ---------> 2 0
    2   5 3 0 3 1 5 ---------> 5 3 0        ---------> [0 2 0 5 3 0 1 2 3 0 i i 1 1 0 i i 5 i 2 0]
    3   1 2 3 0 1 i ---------> 1 2 3 0
    4   i i 1 1 0 2 ---------> i i 1 1 0
    5   i i 5 i 2 0 ---------> i i 5 i 2 0
    '''

    sm[0,0] = 0
    sm[1,0], sm[1,1] = 2, 0
    sm[2,0], sm[2,1], sm[2,2] = 5, 3, 0
    sm[3,0], sm[3,1], sm[3,2], sm[3,3] = 1, 2, 3 ,0
    sm[4,0], sm[4,1], sm[4,2], sm[4,3], sm[4,4] = inf, inf, 1, 1, 0
    sm[5,0], sm[5,1], sm[5,2], sm[5,3], sm[5,4], sm[5,5] = inf, inf, 5, inf, 2, 0

    print('List of important nodes link is \n', sm.data)
    print('Graph matrix is \n', sm.matrix)

    graphMatrix = sm.matrix
    



if __name__ == '__main__':
    main()