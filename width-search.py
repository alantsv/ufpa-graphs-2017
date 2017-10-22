class graph: 
  vertex = [1,2,3,4,5,6,7]
  edge = {1: [2,3],
          2: [1,3],
          3: [1,2,4,5,6,7],
          4: [3,5],
          5: [3,4],
          6: [3],
          7: [3]}

def test_exp_edge(exp_edge, start, close):
  for j1, j2, _ in exp_edge:
    if (j1 == start and j2 == close) or (j2 == start and j1 == close):
      return True
  return False

fifo= []
mark_ver= []
exp_width= []

def width_search(start):
  global fifo
  global mark_ver
  global exp_width

  fifo.append(start)
  mark_ver.append(start)
  
  while(fifo != []):
    v = fifo[0]
    for close in graph.edge[v]:
      if not(close in mark_ver):
        mark_ver.append(close)
        exp_width.append((v, close, "busca"))
        fifo.append(close)
      elif test_exp_edge(exp_width, start, close):
          exp_width.append((start, close, "retorno"))
    fifo.pop(0)
    
  return exp_width
  
for j in width_search(1):
  if (j[2] == "busca"):
    print(j[0], " - ", j[1]," ", j[2])
    
   
