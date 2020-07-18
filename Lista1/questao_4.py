### DFS Version

def bipartido(V, E):
    arbitrary_index = len(V)//2
    v_arbitrary = V[arbitrary_index]
    v_adjacents = get_adjacents(v_arbitrary, E)

    return dfs_can_bipartize(v_arbitrary, v_adjacents[0], E, [v_arbitrary])


def dfs_can_bipartize(initial, current_vertice, E, visited, steps = 1):
    current_adjacents = get_adjacents(current_vertice, E)

    if (steps % 2 == 0) and (initial in current_adjacents):
        return False

    current_adjacents -= visited
    visited.append(current_vertice)
    for adjacent in current_adjacents:
        return dfs_can_bipartize(initial, adjacent, E, visited, steps + 1)
    return True

## Useful Function

def get_adjacents(vertice, edges):
    adjacents = []
    for edge in edges:
        if vertice in edges:
            edge.remove(vertice)
            adjacents += edge
    return adjacents

### Coloring Version

colors = {}

def bipartido_color(V, E):
    for vertice in V:
        colors[vertice] = -1 # sem cor

    for vertice in V:
        if colors[vertice] == -1: # tentar pintar
            if not(can_colorize_vertice(vertice, E, 0)):
                return False
    return True

# colors: 1, 0 e -1 (azul, vermelho e sem cor)
def can_colorize_vertice(vertice, edges, color):
    colors[vertice] = color
    adjacents = get_adjacents(vertice, edges)
    for adjacent in adjacents:
        if colors[adjacent] == -1:
            if not(can_colorize_vertice(adjacent, edges, 1-color)):
                return False
        else:
            if colors[adjacent] == color:
                return False
    return True

