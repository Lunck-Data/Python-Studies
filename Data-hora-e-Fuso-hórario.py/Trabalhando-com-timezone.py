# Trabalhando com timezone

from datetime import datetime, timedelta
import pytz

# Criando datetime com timezone
d = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d) #2025-04-15 14:24:20.713676-03:00

# Trabalhando com time sem library externas