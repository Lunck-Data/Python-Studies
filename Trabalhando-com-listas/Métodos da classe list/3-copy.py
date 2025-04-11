# Faz uma cópia de um objeto.

lista = [1, "Python", [40, 30, 20]]

lista2 = []

lista2 = lista.copy()

print(lista2) # [1, "Python", [40, 30, 20]]

print(id(lista), id(lista2))
#Com esse print, podemos ver que cria uma cópia mas troca a instância. Sendo assim não alterando a original.