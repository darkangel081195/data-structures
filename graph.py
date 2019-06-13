class Graph:
    # ---------------------Nested Vertex class---------------- 
    class Vertex:
        __slots__ = 'value'
        # Constructor to initialize the value
        def __init__(self,value):
            self.value = value
        
        # Returning hashed value of the object to be used as key in map
        def __hash__(self):
            return(hash(id(self)))

    # -------------------Nested Edge class--------------------
    class Edge:
        __slots__ = 'origin','destination','weight'
        #Constructor to initialize the edge
        def __init__(self,origin,dest,value):
            self.origin = origin
            self.dest = dest
            self.weight = value
        
        #Returns the two endpoints of edge
        def endpoints(self):
            return(self.origin,self.dest)
        
        #Returns the other end of the edge if one of the vertex is passed
        def opposite(self,v):
            return self.origin if v is self.dest else self.dest

        #Hasing edge to be used as key in map
        def __hash__(self):
            return(hash(self.origin,self.dest))
    
    #---------------Graph Implementation----------------------------------

    # Constructor of Graph class where the outgoing and incoming maps are initialized
    def __init__(self,directed=False):
        self.directed = directed
        self.out = {}
        self.inc = {} if self.directed else self.out #inc will be only be used in directed is True
    
    #Returns the count of the vertex
    def vertex_count(self):
        return(len(self.out))
    
    # Return iteration of all the vertices of graph
    def vertices(self):
        return self.out.keys()
    
    #Return the total edges
    def edge_count(self):
        total = sum(len(self.out[v])for v in self.out)
        # Return total if its directed else return half
        return total if self.directed else total//2
    
    #Returns the set of edges
    def edges(self):
        #Declaring a set so the same edges are not added in case of undirected graphs
        res = set() 
        for val in self.out.values():
            res.update(val.values())        
        return res
    
    #Return the edge between u and v if it exists
    def get_edge(self,u,v):
        return(self.out[u].get(v,None))
    
    #Returns number of outgoing edges from v in the graph
    def degree(self,v,outgoing = True ):
        adjacent = self.out if outgoing else self.inc
        return(len(adjacent[v]))
    
    #Returns incident edges going from v
    def incident_edges(self,v,outgoing = True):
        # If graph is directed the optional parameter should be passed
        adjacent = self.out if outgoing else self.inc
        for edge in adjacent[v].values():
            yield edge #Generator to return edge one by one
    
    #Inserts a new vertex in the graph
    def insert_vertex(self,val=None):
        vertex = self.Vertex(val) #Creates a vertex object
        self.out[vertex] = {} # Declares a map to store adjacent vertices
        if self.directed:
            self.inc[vertex] = {} #Declare a map for incoming edge for directed graph        
        return vertex
    
    #Creates a new edge between u and v
    def insert_edge(self,u,v,weight=None):
        e = self.Edge(u,v,weight)
        self.out[u][v] = e
        self.inc[v][u] = e

#Depth first search of the graph
def dfs(g,u,discovered):
    #g----->Graph object
    #u------>Starting vertex
    #discovered-------->Map containing discovered vertex along with edge    
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            dfs(g,u,discovered) 
    

          
    

