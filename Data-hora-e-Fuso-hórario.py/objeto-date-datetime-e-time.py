from datetime import date, datetime, time

#date
data = date(2025, 4, 14)
print(data) # 2025-04-14
print(date.today())

#datetime
data_hora = datetime(2025, 4, 14, 10, 15, 1)
print(data_hora) # 2025-04-14 10:15:01
print(datetime.today())

#time
hora = time(10,19,14)
print(hora) #10:19:14