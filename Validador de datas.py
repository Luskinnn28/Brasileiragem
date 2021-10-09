from datetime import datetime, timedelta

hoje = datetime.today() + timedelta()
hojeFormatado = hoje.strftime("%d/%m/%y")
print(hoje)
print(hojeFormatado)
