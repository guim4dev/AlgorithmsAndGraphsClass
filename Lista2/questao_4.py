# LETRA A
def existe_deleta_aresta_estrutura(u, v): # O(2n) - # O(n)
  exists = False
  index_u_adjacents_delete = None
  index_v_adjacents_delete = None
  for adjacente in u.adjacentes:
    adjacente = u.adjacentes[adjacente_index]
    if adjacente == v:
      exists = True
      index_u_adjacents_delete = adjacente_index

  if exists:
    for adjacente_index in range(len(v.adjacentes)):
      adjacente = v.adjacentes[adjacente_index]
      if adjacente == u:
        index_v_adjacents_delete = adjacente_index
    
    del u.adjacentes[index_u_adjacents_delete]
    del v.adjacentes[index_v_adjacents_delete]
    return 'Nós eram adjacentes. Aresta deletada.'
  else:
    return 'Nós não são adjacentes.'

def existe_deleta_aresta_matriz(u, v, matriz_adjacencias): # O(1)
  if matriz_adjacencias[u][v] >= 1:
    matriz_adjacencias[u][v] = 0
    matriz_adjacencias[v][u] = 0

# LETRA B