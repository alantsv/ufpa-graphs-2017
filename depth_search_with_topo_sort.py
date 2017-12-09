class graph:
  def __init__(self):
    self.vertex = list()
    self.edge = dict()

grafo = graph()
grafo.vertex = [1,2,3,4,5,6,7]
grafo.edge = {1: [2,3],
              2: [1,3],
              3: [1,2,3,4,5,6,7],
              4: [3,5],
              5: [3,4],
              6: [3],
              7: [3]}

def test_exp_edge(exp_edge, start, close):
  for j1, j2, _ in exp_edge:
    if (j1 == start and j2 == close) or (j2 == start and j1 == close):
      return False
  return True

mark_ver = []
exp_edge = []
topo_sort = []

def depth_search (graph, start):
  global mark_ver
  global exp_edge
  if not (start in mark_ver): mark_ver.append(start)
  for close in graph.edge[start]:
    if not (close in mark_ver):
      mark_ver.append(close)
      exp_edge.append((start, close, "busca"))
      depth_search(graph, close)
    elif test_exp_edge(exp_edge, start, close):
       exp_edge.append((start, close, "retorno"))
  global topo_sort
  topo_sort = [start] + topo_sort
  return exp_edge

# Main
inital_node = 0
for j in depth_search(grafo2, inital_node):
  if (j[2] == "busca"):
    print(j[0], " - ", j[1]," ", j[2])
print()
print("Topo sort: ", topo_sort)
