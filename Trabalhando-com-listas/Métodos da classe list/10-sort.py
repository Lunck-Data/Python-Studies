# [].sort
# Ordena uma lista

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() #['c', 'csharp', 'java', 'js', 'python']
# Ordenou em ordem alfabetica

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) #['python', 'js', 'java', 'csharp', 'c']
# Ordenou o reverso da ordem alfabetica

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) #['c', 'js', 'java', 'python', 'csharp']
# Ordenou pelo tamanho da String do menor ao maior

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) #['python', 'csharp', 'java', 'js', 'c']
# Ordenou pelo tamanho da String do maior ao menor
