# sorted()
# É semelhante a [].sort mas nesse caso é uma função que realiza a mesma coisa.

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens = sorted(linguagens)
['c', 'csharp', 'java', 'js', 'python']
# Ordena em ordem alfabetica

linguagens = sorted(linguagens, key=lambda x: len(x))
#['c', 'js', 'java', 'python', 'csharp']
# Ordena pelo tamanho da String do menor ao maior

linguagens = sorted(linguagens, key=lambda x: len(x), reverse=True)
#['python', 'csharp', 'java', 'js', 'c']
# Ordena pelo tamanho da String do maior ao menor
