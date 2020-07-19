def misterio(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i**2
        print(s)
    return s

print(misterio(5))

# a) O algoritmo calcula a soma de todos os quadrados de numeros naturais ate n
# b) O(n)
# c) Sugestao abaixo: O(1)

def soma_dos_quadrados(n):
    return n**3/3 + n**2/2 + n/6

print(soma_dos_quadrados(5))