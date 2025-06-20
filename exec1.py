def soma_subconjunto_recursivo(numeros, soma_alvo, indice=0, soma_atual=0, caminho=None):
    if caminho is None:
        caminho = [] 

    if soma_atual == soma_alvo:
        return True, caminho

    if soma_atual > soma_alvo or indice == len(numeros):
        return False, None


    encontrado, resultado_caminho = soma_subconjunto_recursivo(
        numeros, soma_alvo, indice + 1, soma_atual + numeros[indice], caminho + [numeros[indice]]
    )
    if encontrado:
        return True, resultado_caminho

    return soma_subconjunto_recursivo(
        numeros, soma_alvo, indice + 1, soma_atual, caminho
    )

def encontrar_soma_subconjunto(numeros, soma_alvo):
    return soma_subconjunto_recursivo(numeros, soma_alvo)

if __name__ == "__main__":
    numeros1 = [3, 34, 4, 12, 5, 2]
    alvo1 = 9
    encontrado1, subconjunto1 = encontrar_soma_subconjunto(numeros1, alvo1)
    print(f"Conjunto: {numeros1}, Alvo: {alvo1}")
    print(f"Subconjunto encontrado? {encontrado1}")
    if subconjunto1:
        print(f"Subconjunto: {subconjunto1}")

    print("-" * 30)

    numeros2 = [1, 2, 3, 7]
    alvo2 = 6
    encontrado2, subconjunto2 = encontrar_soma_subconjunto(numeros2, alvo2)
    print(f"Conjunto: {numeros2}, Alvo: {alvo2}")
    print(f"Subconjunto encontrado? {encontrado2}")
    if subconjunto2:
        print(f"Subconjunto: {subconjunto2}")

    print("-" * 30)

    numeros3 = [10, 20, 30]
    alvo3 = 15
    encontrado3, subconjunto3 = encontrar_soma_subconjunto(numeros3, alvo3)
    print(f"Conjunto: {numeros3}, Alvo: {alvo3}")
    print(f"Subconjunto encontrado? {encontrado3}")
    if subconjunto3:
        print(f"Subconjunto: {subconjunto3}")