# {}.union
#Junta ambos

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) #{1, 2, 3, 4}


#{}.intersection
#Pega somente as partes iguais

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.intersection(conjunto_d) #{2, 3}


#{}.difference
#Pega somente a diferença do set alvo

conjunto_e = {1, 2, 3}
conjunto_f = {2, 3, 4}

conjunto_e.difference(conjunto_f) # {1}
conjunto_f.difference(conjunto_e) # {4}


#{}.symmetric_difference
#Pega somente a parte diferente de ambos

conjunto_g = {1, 2, 3}
conjunto_h = {2, 3, 4}

conjunto_g.symmetric_difference(conjunto_h) # {1, 4}


#{}.issubset
#Verifica se um conjunto é subconjunto de outro.
#O conjunto i está dentro do conjunto j? True
#O conjunto j está dentro do conjunto i? False

conjunto_i = {1, 2, 3}
conjunto_j = {4, 1, 2, 5, 6, 3}

conjunto_i.issubset(conjunto_j) # True
conjunto_j.issubset(conjunto_i) # False


#{}.isdisjoint
# Verifica se os conjuntos se tocam.
# Exemplo: conjunto k não toca em nenhum elemento o conjunto l
# Já o conjunto k toca no conjunto m. O elemente 1

conjunto_k = {1, 2, 3, 4, 5}
conjunto_l = {6, 7, 8, 9}
conjunto_m = {1, 0}

conjunto_k.isdisjoint(conjunto_l) # True
conjunto_k.isdisjoint(conjunto_m) # False

#{}.add
#Adiciona um elemento ao set, se não exister será adicionado. Se exister será ignorado.

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

#{}.clear
#Função que limpa o set

sorteio = {1, 23}

sorteio # {1,23}
sorteio.clear()
sorteio # {}

#{}.copy
#Cria uma cópia

sorteio = {1, 23}

sorteio # {1,23}
sorteio.clear()
sorteio # {1, 23}

#{}.discard
#Discarta um valor. Se não exister no set, será ignorado.

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.discard(1)
numeros.discard(45)
numeros # {0, 2, 3, 4, 5, 6, 7, 8, 9}


#{}.pop
#Retira o valor da frente. Esquerda para direita.

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop() # 0
numeros.pop() # 1
numeros # {2, 3, 4, 5, 6, 7, 8, 9}


#{}.remove
#Remove o valor desejado. Preciso remover um valor que exista no set, caso não exista dará erro.

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove(0)
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}


#len
#Mostra o tamanho do conjunto.

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
len(numeros) #10]


#in
#Verifica se um objeto está dentro do conjunto

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # True
10 in numeros # False