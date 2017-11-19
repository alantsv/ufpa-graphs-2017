class graph: 
	vertex = ['A','B','C','D','E','F','G','H']
	edge={	'A':{'C': 6, 'D': 12},
        	'B':{'D': 7, 'E':14},
			'C':{'A': 6, 'D': 9, 'F': 16, 'G': 3 },
			'D':{'A': 12, 'B': 7, 'C': 9, 'E': 11},
			'E':{'B': 14, 'D': 11, 'F': 5 , 'H': 18 },
			'F':{'C': 16, 'E': 5, 'G': 8, 'H': 13},
			'G':{'C':3 ,'F': 8, 'H': 20},
        	'H':{'E': 18, 'F': 13, 'G': 20}}
# output = [[6, 'A', 'C'], [7, 'B', 'D'], [3, 'C', 'G'], [5, 'E', 'F'], [13, 'H', 'F'], [8, 'F', 'G'], [9, 'C', 'D']]		
			
	
class graph2: 
	vertex = ['A','B','C','D','E','F','G']
	edge={	'A':{'B': 7, 'D': 4},
        	'B':{'A': 7, 'C': 11, 'D':9, 'E':10},
			'C':{'B': 11, 'E': 5},
			'D':{'A': 4, 'B': 9, 'F': 6},
			'E':{'B': 10, 'C': 5},
			'F':{'D': 6, 'E': 12, 'G':13},
			'G':{'F': 13, 'E': 8}}
## output = [[4, 'A', 'D'], [7, 'B', 'A'], [5, 'C', 'E'], [6, 'F', 'D'], [8, 'G', 'E'], [10, 'B', 'E']]	
   
#função que retorna o peso entre dois vertices
def weigth(grafo,o, d):
	for close in grafo.edge:
		if(close == o):
			aux = grafo.edge[o]
			if d in aux: 
				return aux[d]
	return []

def weigth_min(grafo,vertex):
	min = []
	for close in grafo.edge[vertex]:
		min.append([weigth(grafo,vertex, close),vertex, close])	
	return sorted(min)

#testa se uma ORIGEM e DESTINO já está contido em determinada LISTA
def test_exp_edge(exp_edge, start, close):
	for _, j1, j2 in exp_edge:
		if (j1 == start and j2 == close) or (j2 == start and j1 == close):
			return True
	return False

def weigth_min1(grafo,vertex, list):
	min=[]
	for close in list:
		if(weigth(grafo,vertex, close) != []):
			min.append([weigth(grafo,vertex,close),vertex,close])	
	return sorted(min)

def weigth_min2(grafo, vertex, output):
	min=[]
	for subtree in output:
		if not(vertex in subtree): 
			subtree = weigth_min1(grafo,vertex, subtree)
			if (subtree !=[]):
				min.append(subtree[0])
	return sorted(min)
## verifica se pelo menos um elemento de uma lista está contida em outra
def test_list(a, b):
	for i in a:
		if i in b:
			return True
	return False

#junta duas lista e a retorna ordenada sem repetição
def sortx(list,b):
    l = []
    list.extend(b)
    for i in list:
        if i not in l:
            l.append(i)
    return sorted(l)

## junta duas sublistas, se algum elemento for repetido
def Flatten(list):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if (test_list(list[i],list[j])):
				list[i] = sortx(list[i],list[j])
				list.pop(j)
				return Flatten(list)
	return list


#IMPLEMENTAÇÃO DO ALGORITMO DE BORUVKA 
def boruvka(grafo):
	output = []
	aux = []
	outWithWeigth = []
	for origin in grafo.vertex:
		aux = weigth_min(grafo,origin) 
		weigth, start, close = aux[0]
		if not(test_exp_edge(outWithWeigth,start,close)):
			output.append([start,close])
			outWithWeigth.append([weigth,start,close])	
	while(len(output)>1):
	    aux = []
	    output = Flatten(output)
	    for subtree in output:
	    	for vertex in subtree:
	    		aux.extend(weigth_min2(grafo, vertex, output))
	    aux.sort()	   
	    weigth, start, close = aux[0]
	    output.append(([start,close]))
	    outWithWeigth.append(([weigth,start,close]))
	    output = Flatten(output)
	return(outWithWeigth)

print("Grafo 1: ", boruvka(graph))			
print("\nGrafo 1: ", boruvka(graph2))
		



