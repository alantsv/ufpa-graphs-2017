class graph: 
	vertex = [1,2,3,4,5,6,7,8]
	edge = {1: {3: 26, 5: 38, 7:58, 8:16},
          2: {3: 36, 4: 29, 6: 32, 8:19},
          3: {1: 26, 2: 36, 4: 17, 7: 40, 8:34},
          4: {2: 29, 3: 17, 7:52 },
          5: {1:38, 6: 35, 7: 93, 8:37},
          6: {2: 32, 5: 35, 8:28},
          7: {1: 58, 3: 40, 4:52, 5:93},
          8: {1: 16, 2: 19, 3: 34 , 5:37 , 6:28}}
	
	#saida = [1,8,2,3,4,6,5,7]

"""  
  vertex = [1,2,3,4,5,6]
  edge={	1:{2: 1, 3: 3},
        	2:{1: 1, 3: 1, 4: 1, 5: 4},
        	3:{1: 3, 2: 1, 4: 3, 5: 2},
        	4:{2: 1, 3: 3, 5:-2, 6:1 },
        	5:{2: 4, 3: 2, 4:-2, 6:2},
        	6:{4: 1, 5: 2}}
    #saida == [1,2,3,4,5,6]
"""  
	
#função que retorna o peso entre dois vertices
def weigth(o, d):
	for key in graph.edge:
		if(key == o):
			aux = graph.edge[o]
	return aux[d] 

#testa se uma ORIGEM e DESTINO já está contido em determinada LISTA
def test_exp_edge(exp_edge, start, close):
  for _, j1, j2 in exp_edge:
    if (j1 == start and j2 == close) or (j2 == start and j1 == close):
      return True
  return False

#IMPLEMENTAÇÃO DO ALGORITMO DE PRIM
def prim(start):
	output= []
	aberto= []
	output.append(start)
	
	while(len(output) < len(graph.edge)):
		for key in graph.edge[start]:
			if not(test_exp_edge(aberto, start, key)):
				aberto.append([weigth(start,key), start, key]) 
				aberto = sorted(aberto)
		
		_, j2, j3 = aberto[0]
		if not(j3 in output):
			output.append(j3)
			start = j3
			print()
		else:
			while(j3 in output):
				aberto.pop(0)
				_, j2, j3 = aberto[0]
			output.append(j3)
			start = j3
		aberto.pop(0)
	return output

print(prim(1))
