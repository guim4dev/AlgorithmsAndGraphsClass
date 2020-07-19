###### letra a) // dado: eh bipartido ######

def possui_conjunto_indepente_k(vertices, arestas, k):
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