"""13. Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el 
área y para calcular el volumen utiliza el operador de exponente. """
lado = int(input("Introduce el valor del lado del cubo: "))
area = 6 * (lado ** 2)
volumen = (lado ** 3)
print(area, "este es el valor de el area del cubo")
print(volumen,"este es el valor de el volumen del cubo")
