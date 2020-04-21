#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np


# In[24]:


class Graph:
    def __init__(self, input_vertex_number):
        self.vertex_number = input_vertex_number
        self.edge_number = 0
        self.Adjacency_list = [[] for i in range(self.vertex_number)]
        #print(self.Adjacency_list)
        
    def Add_Path(self, start_vertex, end_vertex, weight=1):
        self.Adjacency_list[start_vertex].append([end_vertex, weight])
        self.edge_number += 1
        
    def Print_List(self):
        print(self.edge_number, "edge(s)")
        for i in range(0, len(self.Adjacency_list)):
            print("Vertex: ", i, " Linked with: ", self.Adjacency_list[i])
            
    def Is_Cyclic(self):
        # check if exist cycle
        vertex_stack = []
        vertex_stack.append(0)
        visited_vertex = set()
        visited_vertex.add(0)
        while (len(vertex_stack) > 0):
            vertex = vertex_stack.pop()
            nodes = []
            for i in range(0, len(self.Adjacency_list[vertex])):
                nodes.append(self.Adjacency_list[vertex][i][0])
            for i in nodes:
                if i in visited_vertex:
                    return True
                else:
                    vertex_stack.append(i)
                    visited_vertex.add(i)
        return False


# In[25]:


input_data = []
file = open('./data/data.txt')
input_vertex_number = int(file.readline())
input_edge_number = int(file.readline())
graph = Graph(input_vertex_number)
for line in file.readlines():
    start_vertex = int(line.split()[0])
    end_vertex = int(line.split()[1])
    weight = float(line.split()[2])
    graph.Add_Path(start_vertex, end_vertex, weight)
file.close()
#graph.Print_List()
graph.Is_Cyclic()


# In[23]:


print(input_vertex_number)
print(input_edge_number)


# In[ ]:





# In[ ]:




