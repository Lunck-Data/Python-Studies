from datetime import datetime

data = datetime.now()

# Formatando data e hora
print(data.strftime("%d/%m/%Y %H:%M")) # 15/04/2025 13:21

# Convertendo string para datetime
mascara = "%d/%m/%Y %H:%M"

date_string = "20/07/2023 15:30"
data = datetime.strptime(date_string, mascara)
print(data) # 2023-07-20 15:30:00