#caixeiro viajante

import itertools

def caixeiro_viajante_forca_bruta(grafo, no_inicial):
    nos = list(grafo.keys())
    nos.remove(no_inicial)

    menor_distancia = float('inf') 
    melhor_caminho = None      

    for permutacao_caminho in itertools.permutations(nos):
        caminho_atual = [no_inicial] + list(permutacao_caminho) + [no_inicial]
        distancia_atual = 0
        rota_valida = True 

        for i in range(len(caminho_atual) - 1):
            u = caminho_atual[i]
            v = caminho_atual[i+1]
            
            if v not in grafo[u]:
                distancia_atual = float('inf') 
                rota_valida = False
                break 
            distancia_atual += grafo[u][v]

        if rota_valida and distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_caminho = caminho_atual

    return menor_distancia, melhor_caminho


grafo_cidades = {
    'Matipo': {'Bh': 10, 'Ponte Nova': 15, 'Rio de Janeiro': 20},
    'Bh': {'Matipo': 10, 'Ponte Nova': 35, 'Rio de Janeiro': 25},
    'Ponte Nova': {'Matipo': 15, 'Bh': 35, 'Rio de Janeiro': 30},
    'Rio de Janeiro': {'Matipo': 20, 'Bh': 25, 'Ponte Nova': 30}
}

cidade_partida = 'Matipo'
dist_min, melhor_rota = caixeiro_viajante_forca_bruta(grafo_cidades, cidade_partida)

print("Grafo de Cidades e Distâncias:")
for cidade, vizinhos in grafo_cidades.items():
    print(f"\n- {cidade}:")
    for destino, distancia in vizinhos.items():
        print(f"   -> {destino}: {distancia} km")

print("-" * 30)

print(f"Cidade de Partida: {cidade_partida}")
print(f"Melhor Rota Encontrada: {melhor_rota}")
print(f"Menor Distância Total: {dist_min}")

print("-" * 30)