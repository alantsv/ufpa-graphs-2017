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

def depth_search (start):
  global mark_ver
  global exp_edge
  if not (start in mark_ver): mark_ver.append(start)
  for close in graph.edge[start]:
    if not (close in mark_ver):
      mark_ver.append(close)
      exp_edge.append((start, close, "busca"))
      depth_search(close)
    elif test_exp_edge(exp_edge, start, close):
       exp_edge.append((start, close, "retorno"))
  return exp_edge

inital_node = 1

for j in depth_search(inital_node):
  if (j[2] == "retorno"):
    print(j[0], " - ", j[1]," ", j[2])
