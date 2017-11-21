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

class graph2:
	vertex = [1,2,3,4,5,6,7,8,9,10]
	edge = {1: {2:6, 3: 1, 4: 14},
			2: {1: 6,3: 10,5: 6, 6: 8} ,
            3: {1:1, 2:10,4:7,6:7 },
            4: {1:14,3:7,6:6,7:6},
            5: {2:6,6:4,8:3  },
            6: {2:8,3:7,4:6,5:4,7:1,8:6,9:5  },
            7: {4:6,6:1,10:5 },
            8: {5:3,6:6,9:6},
            9: {6:5,8:6,10:5},
            10:{7:5,9:5}}
	#saida = [1, 3, 2, 5, 8, 6, 7, 9, 10, 4]

class graph3:
	vertex = [1,2,3,4,5,6]
	edge= { 1:{2: 1, 3: 3},
			2:{1: 1, 3: 1, 4: 1, 5: 4},
        	3:{1: 3, 2: 1, 4: 3, 5: 2},
        	4:{2: 1, 3: 3, 5:-2, 6:1 },
        	5:{2: 4, 3: 2, 4:-2, 6:2},
        	6:{4: 1, 5: 2}}
    #saida == [1,2,3,4,5,6]
  
	
#função que retorna o peso entre dois vertices
def weigth(grafo,o, d):
	for close in grafo.edge:
		if(close == o):
			aux = grafo.edge[o]
	return aux[d] 

#testa se uma ORIGEM e DESTINO já está contido em determinada LISTA
def test_exp_edge(exp_edge, start, close):
  for _, j1, j2 in exp_edge:
    if (j1 == start and j2 == close) or (j2 == start and j1 == close):
      return True
  return False

#IMPLEMENTAÇÃO DO ALGORITMO DE PRIM
def prim(grafo, start):
	output= []
	open= []
	output.append(start)
	
	while(len(output) < len(grafo.edge)):
		for close in grafo.edge[start]:
			if not(test_exp_edge(open, start, close)):
				open.append([weigth(grafo,start,close), start, close]) 
				open.sort()
		_, _, close = open[0]
		if not(close in output):
			output.append(close)
			start = close
		else:
			while(close in output):
				open.pop(0)
				_, _, close = open[0]
			output.append(close)
			start = close
		open.pop(0)
	return output

print("grafo 1: ", prim(graph,1))
print("grafo 2: ", prim(graph2,1))
print("grafo 3: ", prim(graph3,1))


