#!/usr/bin/env python
# coding: utf-8

# In[13]:


#site： https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/


# In[13]:


# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)] 

    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.V): 
            print (node, "\t", dist[node] )

    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 

        # Initilaize minimum distance for next node 
        min = float("inf") 

        # Search not nearest vertex not in the 
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 

        return min_index 

    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation 
    def dijkstra(self, src): 

        dist = [float("inf") ] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 

        for cout in range(self.V): 

            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 

            # Put the minimum distance vertex in the 
            # shotest path tree 
            sptSet[u] = True

            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 

        self.printSolution(dist) 


# In[15]:


Q4b = Graph(8)
matrix = [[0]*8 for i in range(8)]

matrix[4][5] = 0.35
matrix[5][4] = -0.66
matrix[4][7] = 0.37
matrix[5][7] = 0.28
matrix[7][5] = 0.28
matrix[5][1] = 0.32
matrix[0][4] = 0.38
matrix[0][2] = 0.26
matrix[7][3] = 0.39
matrix[1][3] = 0.29
matrix[2][7] = 0.34
matrix[6][2] = 0.40
matrix[3][6] = 0.52
matrix[6][0] = 0.58
matrix[6][4] = 0.93

matrix[5][4] = 0.35
matrix[4][5] = -0.66
matrix[7][4] = 0.37
matrix[7][5] = 0.28
matrix[5][7] = 0.28
matrix[1][5] = 0.32
matrix[4][0] = 0.38
matrix[2][0] = 0.26
matrix[3][7] = 0.39
matrix[3][1] = 0.29
matrix[7][2] = 0.34
matrix[2][6] = 0.40
matrix[6][3] = 0.52
matrix[0][6] = 0.58
matrix[4][6] = 0.93

Q4b.graph = matrix
Q4b.dijkstra(0)


# In[16]:


Q4a = Graph(8)
matrix = [[0]*8 for i in range(8)]

matrix[4][5] = 0.35
matrix[5][4] = 0.35
matrix[4][7] = 0.37
matrix[5][7] = 0.28
matrix[7][5] = 0.28
matrix[5][1] = 0.32
matrix[0][4] = 0.38
matrix[0][2] = 0.26
matrix[7][3] = 0.39
matrix[1][3] = 0.29
matrix[2][7] = 0.34
matrix[6][2] = -1.2
matrix[3][6] = 0.52
matrix[6][0] = -1.4
matrix[6][4] = -1.25

matrix[5][4] = 0.35
matrix[4][5] = 0.35
matrix[7][4] = 0.37
matrix[7][5] = 0.28
matrix[5][7] = 0.28
matrix[1][5] = 0.32
matrix[4][0] = 0.38
matrix[2][0] = 0.26
matrix[3][7] = 0.39
matrix[3][1] = 0.29
matrix[7][2] = 0.34
matrix[2][6] = -1.2
matrix[6][3] = 0.52
matrix[0][6] = -1.4
matrix[4][6] = -1.25

Q4b.graph = matrix
Q4b.dijkstra(0)


# In[ ]:




