#cobertura de vértices

import itertools

def eh_cobertura_vertices(sub_vertices, grafo):
    conjunto_sub_vertices = set(sub_vertices)

    for u in grafo:
        for v in grafo[u]:
            if u not in conjunto_sub_vertices and v not in conjunto_sub_vertices:
                return False
    return True 

def encontrar_menor_cobertura_vertices_forca_bruta(grafo):
    todos_vertices = list(grafo.keys())
    n = len(todos_vertices)

    for k in range(1, n + 1):
        for candidato_subconjunto in itertools.combinations(todos_vertices, k):
            if eh_cobertura_vertices(candidato_subconjunto, grafo):
                return list(candidato_subconjunto)
    
    return []


grafo1 = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C']
}

min_cv1 = encontrar_menor_cobertura_vertices_forca_bruta(grafo1)
print("Grafo 1:")
for vertice, vizinhos in grafo1.items():
    print(f"{vertice} = {', '.join(vizinhos)}")

print("\nResultado da Menor Cobertura:")
print(f"Conjunto de Vértices: {min_cv1}")
print(f"Tamanho da Cobertura: {len(min_cv1)} vértices")