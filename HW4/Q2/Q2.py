#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
# both codes are from https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
#                     https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/?ref=lbp


# In[13]:


# A Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency matrix representation of the graph 


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)] 

    # A utility function to print the constructed MST stored in parent[] 
    def printMST(self, parent): 
        #print ("Edge    \tWeight")
        total_weight = 0
        for i in range(1, self.V): 
            total_weight += self.graph[i][ parent[i] ]
            #print (parent[i], "-", i, " \t", self.graph[i][ parent[i] ]) 
        print("total weight is ", total_weight)

    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree 
    def minKey(self, key, mstSet): 

        # Initilaize min value 
        min = float("inf") 

        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 

        return min_index 

    # Function to construct and print MST for a graph 
    # represented using adjacency matrix representation 
    def primMST(self): 

        # Key values used to pick minimum weight edge in cut 
        key = [float("inf")] * self.V 
        parent = [None] * self.V # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex 
        key[0] = 0
        mstSet = [False] * self.V 

        parent[0] = -1 # First node is always the root of 

        for cout in range(self.V): 

            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration 
            u = self.minKey(key, mstSet) 

            # Put the minimum distance vertex in 
            # the shortest path tree 
            mstSet[u] = True

            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 

        self.printMST(parent) 


# In[14]:


input_data = []
file = open('./data/data.txt')
input_vertex_number = int(file.readline())
input_edge_number = int(file.readline())
graph = Graph(input_vertex_number)
matrix = [[0]*input_vertex_number for i in range(input_vertex_number)]
for line in file.readlines():
    start_vertex = int(line.split()[0])
    end_vertex = int(line.split()[1])
    weight = float(line.split()[2])
    matrix[start_vertex][end_vertex] = weight
    matrix[end_vertex][start_vertex] = weight
graph.graph = matrix
time_start = time.time()
graph.primMST()
time_end = time.time()
print(time_end-time_start, "s")


# In[15]:


# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 

from collections import defaultdict 

#Class to represent a graph 
class Graph: 

    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary 
                                # to store graph 
        

    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        # If ranks are same, then make one as root 
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's 
        # algorithm 
    def KruskalMST(self): 

        result =[] #This will store the resultant MST 

        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 

            # Step 1: Sort all the edges in non-decreasing 
                # order of their 
                # weight. If we are not allowed to change the 
                # given graph, we can create a copy of graph 
        self.graph = sorted(self.graph,key=lambda item: item[2]) 

        parent = [] ; rank = [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
    
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 

            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration 
            u,v,w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            # If including this edge does't cause cycle, 
                        # include it in result and increment the index 
                        # of result for next edge 
            if x != y: 
                e = e + 1    
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            # Else discard the edge 

        # print the contents of result[] to display the built MST 
        #print ("Following are the edges in the constructed MST")
        total_weight = 0
        for u,v,weight in result: 
            #print str(u) + " -- " + str(v) + " == " + str(weight) 
            total_weight += weight
            #print(weight)
            #print ("%d -- %d == %f" % (u,v,weight)) 
        print("total weight is ", total_weight)


# In[16]:


input_data = []
file = open('./data/data.txt')
input_vertex_number = int(file.readline())
input_edge_number = int(file.readline())
graph = Graph(input_vertex_number)
for line in file.readlines():
    start_vertex = int(line.split()[0])
    end_vertex = int(line.split()[1])
    weight = float(line.split()[2])
    graph.addEdge(start_vertex, end_vertex, weight)
time_start = time.time()
graph.KruskalMST()
time_end = time.time()
print(time_end-time_start, "s")


# In[ ]:




