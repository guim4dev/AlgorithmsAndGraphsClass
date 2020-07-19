def possui_ciclo_euleriano(arestas):
    memo = {}
    for aresta in arestas:
        for vertice in aresta:
            memo[vertice] = (memo.get(vertice) or 0) + 1
    for value in memo.values():
        if (value % 2) != 0:
            return False
    return True

# O (m)
