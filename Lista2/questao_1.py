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
def dp_knapsack(P, n, i = -1):
  global dp
  if i == -1:
    i = len(n)

  if dp == []: # montar tabela de Capacidades X Itens
    dp = [[0 for x in range(P+1)] for y in range(len(n)+1)] # montar tabela de Capacidades X Itens

  if i == 0 or P == 0: # caso base
    result = 0
  elif dp[i-1][P] != 0: # aproveitar a memoizacao de operacoes
    return dp[i-1][P]
  elif n[i-1][0] > P:
    result = dp_knapsack(P, n, i-1)
  else:
    included = n[i-1][1] + dp_knapsack(P - n[i-1][0], n, i-1)
    not_included = dp_knapsack(P, n, i-1)

    result = max(included, not_included)
  dp[i][P] = result
  return(result)

def get_dp_knapsack_array(P, n):
  result = dp_knapsack(P, n)
  res = result
  items = []
  p = P 
  for i in range(len(n), 0, -1): 
    if res <= 0: 
      break
    # either the result comes from the 
    # top (K[i-1][w]) or from (val[i-1] 
    # + K[i-1] [w-wt[i-1]]) as in Knapsack 
    # table. If it comes from the latter 
    # one/ it means the item is included. 
    if res == dp[i - 1][p]: 
      continue
    else: 
      # Item incluido 
      items.append(n[i-1])
      res = res - n[i - 1][1] 
      p = p - n[i - 1][0]
  return(result, items) 

print(get_dp_knapsack_array(P, coisas))

# Complexidade Tempo: O(n*P) - n: numero de elementos, P: capacidade desejada
# Complexidade Espaco: O(n*P) - matriz auxiliar criada
