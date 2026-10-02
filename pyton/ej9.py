#9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos = int(input("Introduce un número de segundos: "))
minutos = segundos // 60
horas = minutos // 60
print(f"En {segundos} segundos hay {minutos} minutos y {horas} horas.")