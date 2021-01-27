from datetime import date
from datetime import datetime

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)


# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

print("\nHoje",datetime.now())
print("Data",datetime.now().date())
print("Tempo",datetime.now().time())
print("Ano",datetime.now().year)
print("Mes",datetime.now().month)
print("Dia",datetime.now().day)
print("Hora",datetime.now().hour)
print("Minutos",datetime.now().minute)
print("Sugundos",datetime.now().second)
print("Microsegundos",datetime.now().microsecond)