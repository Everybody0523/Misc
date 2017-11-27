class Graph:
    """
    Class for a Graph. By default, these are actually directed graphs.
    Graphs are represented with adjacency tables...or rather, adjacency
    dictionaries.

    (Note that by Graph, I mean in the "Verticies and Edges" sense, not
    the "Visual representation of a function" sense. Which should be pretty
    clear with a cursorary glance at the code, but hey.)
    """
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict

    def addVertex(self, value):
        if value in self.graph_dict:
            print("Already in graph!")
            return False
        else:
            self.graph_dict[value] = []
            return True

    def addEdge(self, edge):
        """
        Add an edge e = (v1, v2) to the graph. v1 and v2 should be verticies
        already in the graph.

        Returns True on successful addition of verticies, and False otherwise.
        """
        (vertex1, vertex2) = tuple(edge)
        if not((vertex1 in self.graph_dict) and (vertex2 in self.graph_dict)):
            print("PUT THE DAMN VERTICIES IN FIRST")
            return False
        self.graph_dict[vertex1].append(vertex2)
        return True


class UndirectedGraph(Graph):
    """
    An undirected graph. Extends class Graph.
    """
    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if not((vertex1 in self.graph_dict) and (vertex2 in self.graph_dict)):
            print("PUT THE DAMN VERTICIES IN FIRST")
            return False
        self.graph_dict[vertex1].append(vertex2)
        self.graph_dict[vertex2].append(vertex1)
        return True


    def getVertices(self):
        return list(self.graph_dict.keys())


    def getEdges(self):
        edges = []
        for v in self.graph_dict:
            for v1 in self.graph_dict[v]:
                edges.append((v, v1))
        return edges


    def depthFirstTraversal(self, start, path):
        """
        Traverse a graph in depth-first order.

        Arguments:
            start - The node you wish to start at
            path - A list of already visited nodes for a path. When calling
                   this function, MAKE IT EMPTY.
        Returns:
            path - a list of integers indicating the order in which the graph
                   was traversed in.
        """
        if start not in self.graph_dict:
            return []
        else:
            path.append(start)
            for node in self.graph_dict[start]:
                if not node in path:
                    path = self.depthFirstTraversal(node, path)
            return path


    def isTree(self, start, visited):
        if visited == {}:
            for n in self.graph_dict:
                visited[n] = 0
        if not self.graph_dict[start]:
            return True
        else:
            visited[start] += 1
            for node in self.graph_dict[start]:
                #if not node in visited:
                visited[node] += 1
                if (visited[node] < len(self.graph_dict[node])):
                    if not self.isTree(node, visited):
                        return False
            for d in visited:
                if visited[d] > len(self.graph_dict[d]):
                    return False
            return True


    def __str__(self):
        output = ""
        output += "A graph is a pair of sets: {E (Edges), V (Verticies)}\n"
        output += "V is:\n"
        output += "{"
        x = self.getVertices()
        output += str(x)
        output += "}"
        output += "\n"
        output += "E is: \n"
        y = self.getEdges()
        output += "{"
        output += str(y)
        output += "}"
        return output
