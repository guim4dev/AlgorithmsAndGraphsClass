###### letra a) // dado: eh bipartido ######
# O (n) - Polinomial

def possui_conjunto_independente_k(vertices, arestas, k):
    vertices_colors = colorized_vertices(vertices, arestas)
    independent_one = []
    independent_zero = []
    for key, value in vertices_colors:
        if value == 1:
            independent_one.append(key)
        elif value == 0:
            independent_zero.append(key)
    if (len(independent_one) >= k) or (len(independent_zero) >= k):
        return True
    return False

# Useful functions
def get_adjacents(vertice, edges):
    adjacents = []
    for edge in edges:
        if vertice in edges:
            edge.remove(vertice)
            adjacents += edge
    return adjacents

colors = {}

def colorized_vertices(V, E):
    for vertice in V:
        colors[vertice] = -1 # sem cor

    for vertice in V:
        if colors[vertice] == -1: # tentar pintar
            colorize_vertice(vertice, E, 0)
    return colors

# colors: 1, 0 e -1 (azul, vermelho e sem cor)
def colorize_vertice(vertice, edges, color):
    colors[vertice] = color
    adjacents = get_adjacents(vertice, edges)
    for adjacent in adjacents:
        if colors[adjacent] == -1:
            colorize_vertice(adjacent, edges, 1-color)
    return True

###### letra b) fazer ######

def possui_ciclo_hamiltoniano(V,E):
    posible_starts = get_posible_starts(E)
    for start in posible_starts:
        adjacents = get_adjacents(start, E)
        if can_cycle(start, adjacents, V, E):
            return True
    return False

def can_cycle(start, start_adjacents, V, E):
    edges = edges_without_vertice(E, start)
    vertices = V - [start]
    posible_pairs = [(start_adjacents[i], start_adjacents[j]) for i in range(len(start_adjacents)) for j in range(i+1, len(start_adjacents))]
    for pair in posible_pairs:
        adjacent_start = pair[0]
        adjacent_end = pair[1]
        if has_hamilton_path(adjacent_start, adjacent_end, vertices, edges):
            return True
    return False

def has_hamilton_path(current, end, V, E, visited = []):
    adjacents = get_adjacents(current, V)
    visited.append(current)
    ways = adjacents - visited
    if ways == [end]:
        return True
    ways -= [end]
    for way in ways:
        if has_hamilton_path(way, end, V, E, visited):
            return True
    return False

def edges_without_vertice(E, vertice):
    edges = []
    for edge in E:
        if vertice in edge:
            next
        edges.append(edge)
    return edges
def get_posible_starts(edges):
    posibles = []
    memo = {}
    for edge in edges:
        for vertice in edge:
            memo[vertice] = (memo.get(vertice) or 0) + 1
    for key, value in memo:
        if value > 1:
            posibles.append(key)
    return posibles
