import networkx as nx  #this module should be installed before use
import numpy as np
import matplotlib.pyplot as plt  #this module should be installed before use

d = int(input("Please enter matrix dimetion: "))

matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(d):          # A for loop for row entries
    a =[]
    for j in range(d):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)

graph_simplity = True
graph_connectivity = True

for i in range(d):
    for j in range(d):
        
        if matrix[i][j] > 1:
            graph_simplity = False
            
        elif matrix[i][j] == 0 :
            if i != j:
                graph_connectivity = False

if graph_simplity == False and graph_connectivity == False:
    print("Graph is not simple and is not connected\nplease try again")
    exit()
    
elif graph_simplity == False:
    print("Graph is not simple\nplease try again") 
    exit() 
    
elif graph_connectivity == False:
    print("Graph is not connected\nplease try again") 
    exit()

class SimpleGraph:
     
    adj = []
 
    def __init__(self, v, e):
         
        self.v = v
        self.e = e
        SimpleGraph.adj = matrix
 
    # Function to add an edge to the graph
    def addEdge(self, start, e):
         
        # Considering a bidirectional edge
        SimpleGraph.adj[start][e] = 1
        SimpleGraph.adj[e][start] = 1
 
    # Function to perform DFS on the graph
    def DFS(self, start, visited):
         
        # Print current node
        print(start, end = ' ')
 
        # Set current node as visited
        visited[start] = True
 
        # For every node of the graph
        for i in range(self.v):
             
            # If some node is adjacent to the
            # current node and it has not
            # already been visited
            if (SimpleGraph.adj[start][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited)
    
    def BFS(self, start):
         
        # Visited vector to so that a
        # vertex is not visited more than
        # once Initializing the vector to
        # false as no vertex is visited at
        # the beginning
        visited = [False] * self.v
        q = [start]
 
        # Set source as visited
        visited[start] = True
 
        while q:
            vis = q[0]
 
            # Print current node
            print(vis, end = ' ')
            q.pop(0)
             
            for i in range(self.v):
                if (SimpleGraph.adj[vis][i] == 1 and
                      (not visited[i])):
                           
                    # Push the adjacent node
                    # in the queue
                    q.append(i)
                     
                    visited[i] = True
 
 
# Create the graph
directed_graph = nx.DiGraph()
graph = SimpleGraph(d, d*(d-1)/2)
i = 0
j = 1
edges_list = []
while j < d:
    edges_list.append((str(i),str(j)))
    j += 1
    if j ==d :
        i += 1
        j = i + 1

    

 
# Visited vector to so that a vertex is not visited more than once
visited = [False] * d
 
graph.DFS(0, visited)
print()

graph.BFS(0)
print()



np_matrix = np.matrix(matrix)
h = nx.from_numpy_matrix(np_matrix)
nx.draw(h)
plt.show()    #this will show simple graph in new window

directed_graph.add_edges_from(edges_list)
nx.draw(directed_graph)
plt.show()    # this will show directed graph in new window

     
     

 