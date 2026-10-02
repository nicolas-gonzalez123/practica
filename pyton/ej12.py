"""12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro. """
lado=int(input("Introduce el valor del lado del trapecio: "))
base_menor=int(input("Introduce el valor de la base menor: "))
base_mayor=int(input("Introduce el valor de la base mayor: "))
altura=int(input("Introduce el valor de la altura: "))
area=((base_menor+base_mayor)*altura)/2
perimetro=2*lado+base_menor+base_mayor
print(f"El área del trapecio es {area} y el perímetro es {perimetro}.")