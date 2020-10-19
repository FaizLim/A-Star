class Vertex:
  """Key methods of Vertex class"""
  def __init__(self, value):
      self.value = value
      self.edges = {}
  def add_edge(self, vertex, weight = 0):
      self.edges[vertex] = weight
  def get_edges(self):
      return self.edges

class Graph:
  """Key methods of Graph class"""
  def __init__(self):
      self.graph_dict = {}
  def add_vertex(self, vertex):
      self.graph_dict[vertex.value] = vertex
  def add_edge(self, from_vertex, to_vertex, weight = 0):
      self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
  def print_graph(self):
      print(self.graph_dict.keys())


A = Vertex('f')
B = Vertex('a')
C = Vertex('i')
D = Vertex('z')

Word = Graph()
Word.add_vertex(A)
Word.add_vertex(B)
Word.add_vertex(C)
Word.add_vertex(D)
Word.print_graph()



