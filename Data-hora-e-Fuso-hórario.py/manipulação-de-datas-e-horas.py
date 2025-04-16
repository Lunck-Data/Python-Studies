from datetime import datetime, timedelta

# Criando data e hora
data = datetime(2023, 7, 19, 13, 45)
print(data) # 2023-07-19 13:45:00

data = data + timedelta(days = 5)
print(data) # 2023-07-24 13:45:00

data = data + timedelta(hours = 2)
print(data) # 2023-07-24 15:45:00

data = data + timedelta(weeks = 4)
print(data) # 2023-08-21 15:45:00

tipo_carro = "M" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual - timedelta(minutes= tempo_pequeno)
    print(f"O carro chegou: {data_atual}. \nFicará pronto {data_estimada}.")

if tipo_carro == "M":
    data_estimada = data_atual - timedelta(minutes= tempo_medio)
    print(f"O carro chegou: {data_atual}. \nFicará pronto {data_estimada}.")

if tipo_carro == "G":
    data_estimada = data_atual - timedelta(minutes= tempo_grande)
    print(f"O carro chegou: {data_atual}. \nFicará pronto {data_estimada}.")