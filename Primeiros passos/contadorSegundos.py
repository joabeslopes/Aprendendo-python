total_segs = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = total_segs // 86400
horas = (total_segs % 86400) // 3600
minutos = (total_segs % 3600) // 60
segs = total_segs % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs, "segundos.")
