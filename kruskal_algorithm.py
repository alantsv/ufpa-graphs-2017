class graph:
  vertex = [1,2,3,4,5,6,7,8]
  edge = {1: {3: 26, 5: 38, 7: 58, 8: 16},
          2: {3: 36, 4: 29, 6: 32, 8: 19},
          3: {1: 26, 2: 36, 4: 17, 7: 40, 8: 34},
          4: {2: 29, 3: 17, 7: 52 },
          5: {1: 38, 6: 35, 7: 93, 8: 37},
          6: {2: 32, 5: 35, 8: 28},
          7: {1: 58, 3: 40, 4: 52, 5: 93},
          8: {1: 16, 2: 19, 3: 34, 5: 37 , 6: 28}}
          
def weigth(graph, start, close):
  return graph.edge[start][close]

def sort_weight(graph):
  weight_sorted = []
  for start in graph.vertex:
    for close in graph.edge[start]:
      weight_sorted.append([ start, close, weigth(graph, start, close)])
  weight_sorted = sorted(weight_sorted, key=lambda weight_sorted: weight_sorted[2])
  return weight_sorted

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
  for close in graph[start]:
    if not (close in mark_ver):
      mark_ver.append(close)
      exp_edge.append((start, close, "busca"))
      depth_search(graph, close)
    elif test_exp_edge(exp_edge, start, close):
       exp_edge.append((start, close, "retorno"))
  global topo_sort
  topo_sort = [start] + topo_sort
  return exp_edge

def cycle(egraph, close):
  graph =  egraph.copy()
  global mark_ver
  global exp_edge
  global topo_sort
  exp_edge = []
  mark_ver = []
  topo_sort = []
  if (close[1] not in graph):
    graph[close[1]] = [close[0]]
  if close[0] in graph: 
    graph[close[0]] = graph[close[0]] + [close[1]]
  else:
    graph[close[0]] = [close[1]]
  dgraph = depth_search(graph, 1)
  for element in dgraph:
    if element[2] == 'retorno':
      return True
  return False
  

def kruskal(graph):
  graph_sorted = sort_weight(graph)
  minimal_tree = {}
  minimal_tree[graph_sorted[0][0]] = [graph_sorted[0][1]]
  i = 1
  while len(minimal_tree) < len(graph.edge):
    if not (cycle(minimal_tree, graph_sorted[i])):
      if graph_sorted[i][0] not in minimal_tree:
        minimal_tree[graph_sorted[i][0]] = [graph_sorted[i][1]] 
      else:
        minimal_tree[graph_sorted[i][0]] = minimal_tree[graph_sorted[i][0]] + [graph_sorted[i][1]]
    i += 1
  return minimal_tree

print(kruskal(graph))
