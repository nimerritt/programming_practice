import random

class Vertex:
    """ Represents a vertex in a graph. """
    def __init__(self, neighbours = []):
        self.neighbours = neighbours

class Graph:
    """ A Graph is a set of vertices with its edges are defined implicitly by
    the list of neighbours for each vertex. """

    def __init__(self, vertices = []):
        self.vertices = vertices


def random_graph(num_vertices = 10):
    """ Construct a random *directed* graph by randomly picking a subset of
    vertices as neighbours for each vertex. May contain self-loops. """

    vertices = [Vertex() for i in range(num_vertices)]
    # pick random subset as neighbours
    for vertex in vertices:
        degree = random.randint(0, num_vertices // 2)
        vertex.neighbours = random.sample(vertices, degree)

    return Graph(vertices)


def bfs(start, on_visit):
    """ Takes a start vertex and calls on_visit for each vertex. Transverses
    the graph in a breadth-first manner. If on_visit returns False, we stop 
    the search.  """

    to_visit = [start]
    visited = {}

    while to_visit:
        current = to_visit.pop()
        visited[current] = True
        unvisited_neighbours = [n for n in current.neighbours if n not in visited]
        to_visit.extend(unvisited_neighbours)
        on_visit(current)

def path_exists(start, end):
    # bfs until end is visited, or we finish
    found = False
    # closure to pass to bfs routine
    def found_end(vertex):
        nonlocal found
        if vertex == end:
            found = True
            return False # abort search
        return True # continue search 

    bfs(start, found_end)
    return found

def check_random_graph():
    g = random_graph()
    start = random.choice(g.vertices)
    end = random.choice(g.vertices)

    print("Searching for path between {} and {}".format(start, end))
    if path_exists(start, end):
        print("Found a path")
    else:
        print("No path exists")

def linear_graph(n = 10):
    vertices = [Vertex() for i in range(n)]
    for i in range(len(vertices) - 1):
        vertices[i].neighbours = [vertices[i+1]]
    return Graph(vertices)

def check_linear_graph():
    n = 10
    g = linear_graph(n)
    start = g.vertices[0]
    end = g.vertices[n-1]
    if path_exists(start, end):
        print("Path exists in linear graph... good")
    else:
        print("woops, something must be wrong. A path should exist in the linear graph")

check_linear_graph()
check_random_graph()
