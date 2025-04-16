#{}.clear
#Limpa o dicionário

contatos= {
    "luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},
    "maria@gmail.com" : {"nome": "Maria", "telefone": "4002-8922"},
}

contatos.clear()
contatos # {}


#{}.copy
#Cópia o dicionário

contatos = {
    "luan@gmail.com": {"nome": "Luan", "telefone": "4002-0922"}
}

copia = contatos.copy()
copia["luan@gmail.com"] = {"nome": "Lu"}

contatos["luan@gmail.com"] #{"nome": "Luan", "telefone": "4002-0922"}
copia["luan@gmail.com"] #{"nome": "Lu"}


#{}.fromkeys
#Adiciona um valor a todos elementos do dicionario. Pode ser um dicionário existento ou não

dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}


#{}.get
#Se eu tento buscar uma chave e ela não exister dará o erro KeyError, mas se eu utilizar .get
#Retorna o valor vazio caso não exista, e se exister retorna o valor da chave.

contatos.clear()

contatos = {
    "luan@gmail.com": {"nome": "Luan", "telefone": "4002-0922"}
}

#contatos["chave"]    #KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("luan@gmail.com", {}) #{'nome': 'Luan', 'telefone': '4002-0922'}


#{}.items
#Ela retorna uma lista de tuplas

contatos.clear()

contatos = {
    "luan@gmail.com": {"nome": "Luan", "telefone": "4002-0922"}
}

contatos.items() #dict_items([('luan@gmail.com', {'nome': 'Luan', 'telefone': '4002-0922'})])


#{}.keys
#Retorna somente as chaves do dicionário
contatos.clear()

contatos= {
    "luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},
    "maria@gmail.com" : {"nome": "Maria", "telefone": "4002-8922"},
}

contatos.keys() #dict_keys(['luan@gmail.com', 'giovana@gmail.com', 'guilherme@gmail.com', 'maria@gmail.com'])


#{}.pop
#Retorna e remove a chave do dicionário

contatos.clear()

contatos= {
    "luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},
    "maria@gmail.com" : {"nome": "Maria", "telefone": "4002-8922"},
}

contatos.pop("maria@gmail.com")
#'luan@gmail.com': {'nome': 'Luan', 'telefone': '3333-2221'}, 
#'giovana@gmail.com': {'nome': 'Giovana', 'telefone': '3333-2222'}, 
#'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2223'}

contatos.pop("maria@gmail.com", {})
#Como Maria@gmail.com não existe mais, irá retornar o valor {Vazio}
#Se por acaso não colocarmos um valor de retorno, dará erro.


#{}.popitem
#Se não der um valor para remoção, irá tirar o item por ordem de pilha.

contatos.clear()

contatos= {
    "luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},
    "maria@gmail.com" : {"nome": "Maria", "telefone": "4002-8922"},
}

contatos.popitem()
#"luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
#"giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
#"guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},


#{}.setdefault
#Ele adiciona um valor a chave da váriavel, caso já tenha um valor, ele retorna e utiliza ele.

contato = {'nome': 'Luan', 'Telefone': '4002-8922'}

contato.setdefault("nome", "Paloma") #"Luan"
contato #{'nome': 'Luan', 'Telefone': '4002-8922'}

contato.setdefault("idade", 26) #26
contato #{'nome': 'Luan', 'Telefone': '4002-8922', 'idade': 26}


#{}.update
#Ele deixa a gente atualizar nosso dicionário, com outro dicionário.

contatos.clear()
contatos = {
    "luan@gmail.com": {"nome": "Luan", "telefone": "4002-8922"}
}

contatos.update({"luan@gmail.com": {"nome": "Lu"}})
contatos #"luan@gmail.com": {"nome": "Lu", "telefone": "4002-8922"}

contatos.update({"paloma@gmail.com": {"Nome": "Paloma", "telefone": "2341-3241"}})
contatos
#{"luan@gmail.com": {"nome": "Luan", "telefone": "4002-8922"}
#{"paloma@gmail.com": {"Nome": "Paloma", "telefone": "2341-3241"}


#{}.values
#Retorna todos valores do dicionário. Semelhante ao {}.keys que retorna somente as chaves.

contatos.clear()

contatos= {
    "luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},
    "maria@gmail.com" : {"nome": "Maria", "telefone": "4002-8922"},
}

contatos.values()
#dict_values([{'nome': 'Luan', 'telefone': '3333-2221'}, 
# {'nome': 'Giovana', 'telefone': '3333-2222'}, 
# {'nome': 'Guilherme', 'telefone': '3333-2223'}, 
# {'nome': 'Maria', 'telefone': '4002-8922'}])


#in 
#Verifica se tem a chave informado no dicionário

contatos.clear()

contatos= {
    "luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},
    "maria@gmail.com" : {"nome": "Maria", "telefone": "4002-8922"},
}

"luan@gmail.com" in contatos # True
"paloma@gmail.com" in contatos # False
"idade" in contatos["luan@gmail.com"] # False
"telefone" in contatos["luan@gmail.com"] # True


#del
#Remove um chave ou valor do dicionário

contatos.clear()

contatos= {
    "luan@gmail.com" : {"nome": "Luan", "telefone": "3333-2221"},
    "giovana@gmail.com" : {"nome": "Giovana", "telefone": "3333-2222"},
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2223"},
    "maria@gmail.com" : {"nome": "Maria", "telefone": "4002-8922"},
}

del contatos["luan@gmail.com"]["telefone"]
del contatos["maria@gmail.com"]

contatos
#{'luan@gmail.com': {'nome': 'Luan'}, 
#'giovana@gmail.com': {'nome': 'Giovana', 'telefone': '3333-2222'}, 
#'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2223'}}