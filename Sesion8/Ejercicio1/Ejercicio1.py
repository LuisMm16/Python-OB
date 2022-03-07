# Crear un archivo txt, abrir y escribir

# Creamos y escribimos
f = open('ejercicio.txt', 'w')
f.write('Comunicacion sin emocion')
f.close()

# Abre el archivo creado e imprime por consola
f = open('ejercicio.txt', 'r')
datos = f.read()
print(datos)