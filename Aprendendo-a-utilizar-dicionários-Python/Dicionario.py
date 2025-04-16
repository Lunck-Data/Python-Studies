#Criando dicionários

pessoa = {"nome": "Luan", "idade": 26}
print(pessoa)

pessoa = dict(nome="Luan", idade=26)
print(pessoa)

pessoa["telefone"] = "3333-1234" #{"nome": "Guilherme", "idade":28, "telefone": "3333-1234"}
print(pessoa)



#Acessando dados

dados = {"nome": "Luan Vieira", "idade": 26, "telefone": "3333-1234"}

dados["nome"] # "Luan Vieira"
dados["idade"] # 28
dados["telefone"] # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "4002-8922"

dados #{"nome": "Maria", "idade": 18, "telefone": "4002-8922"}


#Dicionários aninhados

contatos= {
    "luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},
    "maria@gmail.com" : {"nome": "Maria", "telefone": "4002-8922"},
}

print(contatos["maria@gmail.com"]["telefone"]) #4002-8922


#Iterar dicionários

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

#luan@gmail.com {'nome': 'Luan', 'telefone': '3333-2221'}
#giovana@gmail.com {'nome': 'Giovana', 'telefone': '3333-2222'}
#guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2223'}
#maria@gmail.com {'nome': 'Maria', 'telefone': '4002-8922'}