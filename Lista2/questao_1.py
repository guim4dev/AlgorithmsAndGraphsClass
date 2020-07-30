# P = limite
# n = lista de objetos
# i = iterador (algoritmo eh recursivo)
# objeto = [p, v], sendo p = peso e v = valor
def greedy_knapsack(P, n, i = -1, final_array = []): # LETRA A
  if i == -1: # setar iterador na primeira chamada conforme tamanho do array de itens
    i = max((len(n) - 1), 0)
 
  if i == 0 or P == 0: # caso base
    return [0, final_array]

  # maximo entre dois casos:
  if n[i][0] > P: # peso do item > capacidade do knapsack - nao podemos incluir
    return greedy_knapsack(P, n, i-1)
  else: # maximo entre dois casos:
    # item atual incluido e item atual nao incluido
    included_call = greedy_knapsack(P-n[i][0], n, i-1, final_array + [n[i]])
    included = n[i][1] + included_call[0] # valor maximo quando incluido este item
    not_included_call = greedy_knapsack(P, n, i-1, final_array) 
    not_included = not_included_call[0] # valor maximo quando nao incluido

    if included > not_included:
      return [included, included_call[1]]
    else:
      return not_included_call

coisas = [[10, 60], [20, 100], [30, 120], [80, 1000], [20, 100]] 
P = 80
print(greedy_knapsack(P, coisas)) # retorna array com valor dentro do knapsack e array dos objetos dentro do knapsack 

# Complexidade: O(2^n)

dp = []
def dp_knapsack(P, n, i = -1, final_array = []):
  global dp

  if i == -1:
    i = len(n) - 1

  if dp == []: # montar tabela de Capacidades X Itens
    dp = [[None for x in range(P+1)] for y in range(len(n))] # montar tabela de Capacidades X Itens

  if dp[i][P] != None: return dp[i][P] # aproveitar a memoizacao de operacoes

  if i == 0 or P == 0: # caso base
    result = [0, final_array]
  elif n[i][0] > P:
    result = dp_knapsack(P, n, i-1, final_array)
  else:
    included_call = dp_knapsack(P - n[i][0], n, i-1, final_array + [n[i]])
    included = n[i][1] + included_call[0]
    not_included_call = dp_knapsack(P, n, i-1, final_array)
    not_included = not_included_call[0]

    if included > not_included:
      result = [included, included_call[1]]
    else:
      result = not_included_call
  dp[i][P] = result
  return result

print(dp_knapsack(P, coisas))

# Complexidade Tempo: O(n*P) - n: numero de elementos, P: capacidade desejada
# Complexidade Espaco: O(n*P) - matriz auxiliar criada
