#Grafo de exemplo com ciclo negativo
class graph: 
	vertex = [1,2,3,4,5,6]
	edge={	1 : {2 : 1, 3 : 3},
			2 : {3 : 1, 4 : 3, 5 : 2},
			3 : {4 : 2},
			4 : {4 :-1, 6 : 2},
			5 : {4 : -3},
			6 : {5 : 3}}


# Grafo de exemplo
class graph2: 
	vertex = {"s", "t", "x", "y", "z"}
	edge={	's' : {'t' : 6, 'y' : 7},
			't' : {'x' : 5, 'y' : 8, 'z' : -4},
			'x' : {'t' : -2},
			'y' : {'x' : -3, 'z' : 9},
			'z' : {'s' : 2, 'x' : 7}}


def get_edges(graph):
	aux = []
	for i in graph.edge:
		for j in graph.edge[i]:  
			aux.append([i, j , graph.edge[i][j]])
	return(aux)
	
def BF (G, vi, vf):
	# inicialização
	distance = {}
	way = {}
	for j in G.vertex:
		distance[j] = float('inf')
		way[j] = -1
	
	distance[vi] = 0
	
	edges = get_edges(G)
#	relaxamento das arestas
	for i in range(1, len(G.edge) -1):
		for origin, destiny, weight in edges:
			if (distance[destiny] > distance[origin] + weight):
				distance[destiny] = distance[origin] + weight
				way[destiny] = origin 
	
	negative_cycle = False
	
	#verificação de ciclos negativos
	for origin, destiny, weight in edges:
		if distance[destiny] > distance[origin] + weight:
			negative_cycle = True
			if negative_cycle:
				break
			
	# preparando o resultado final
	if not(negative_cycle):
		fim = way[vf]
		res = '' 
		while(fim[0] != vi):
			res = fim[0] + res
			fim = way[fim[0]]
		print("Menor distância de " + vi + " até " + vf + " : "+ vi + res + vf,". Valor = ", distance[vf],".")
	else:
		print("Impossível calcular. Há ciclos negativos.")
		
			
BF(graph2, 's', 'z')
print("-----")
BF(graph, 1, 6)
