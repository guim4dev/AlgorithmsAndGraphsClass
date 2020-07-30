# P = limite
# n = lista de objetos
# i = iterador (algoritmo eh recursivo)
# objeto = [p, v], sendo p = peso e v = valor
final_array_indexes = set()
def greedy_knapsack(P, n, i = -1): # LETRA A
  global final_array_indexes
  if i == -1: # setar iterador na primeira chamada conforme tamanho do array de itens
    i = max((len(n) - 1), 0)
 
  if i == 0 or P == 0: # caso base
    return 0

  # maximo entre dois casos:
  if n[i][0] > P: # peso do item > capacidade do knapsack - nao podemos incluir
    return greedy_knapsack(P, n, i-1)
  else: # maximo entre dois casos:
    # item atual incluido e item atual nao incluido
    included = n[i][1] + greedy_knapsack(P-n[i][0], n, i-1) # valor maximo quando incluido este item
    not_included = greedy_knapsack(P, n, i-1) # valor maximo quando nao incluido

    if included > not_included:
      final_array_indexes = final_array_indexes.union({i})
      return included
    else:
      return not_included

def get_knapsack_array(P, n, algo = 'greedy'):
  final_array = []
  if algo == 'greedy':
    greedy_knapsack(P, n)
  elif algo == 'dp':
    dp_knapsack(P, n)

  for i in final_array_indexes:
    final_array.append(n[i])
  return final_array

coisas = [[10, 60], [20, 100], [30, 120]] 
P = 50
print(greedy_knapsack(P, coisas)) # retorna valor dentro do knapsack 
print(get_knapsack_array(P, coisas, 'greedy')) # retorna o subconjunto dos objetos - passandro greedy pegamos com algoritmo guloso

# Complexidade: O(2^n)

dp = []
def dp_knapsack(P, n, i = -1):
  global dp
  global final_array_indexes

  if i == -1:
    i = len(n) - 1

  if dp == []: # montar tabela de Capacidades X Itens
    dp = [[None for x in range(P+1)] for y in range(len(n))] # montar tabela de Capacidades X Itens

  if dp[i][P] != None: return dp[i][P] # aproveitar a memoizacao de operacoes

  if i == 0 or P == 0: # caso base
    result = 0
  elif n[i][0] > P:
    result = dp_knapsack(P, n, i-1)
  else:
    included = n[i][1] + dp_knapsack(P - n[i][0], n, i-1)
    not_included = dp_knapsack(P, n, i-1)

    if included > not_included:
      final_array_indexes = final_array_indexes.union({i})
      result = included
    else:
      result = not_included
  dp[i][P] = result
  return result

final_array_indexes.clear()
print(dp_knapsack(P, coisas))
print(get_knapsack_array(P, coisas, 'dp')) # retorna o subconjunto dos objetos - passandro dp pegamos com algoritmo de programacao dinamica

# Complexidade Tempo: O(n*P) - n: numero de elementos, P: capacidade desejada
# Complexidade Espaco: O(n*P) - matriz auxiliar criada
