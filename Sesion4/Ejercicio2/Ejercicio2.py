# Imprimir en pantalla numeros impares desde un inicio hasta un final

# Convierte a entero el numero ingresado
numero_inicial = int(input("Ingrese el número inicial: "))
numero_final = int(input("Ingrese el número final: "))

if numero_inicial % 2 == 0: # Si el numero es par, suma uno para empezar desde el numero impar
    numero_inicial += 1
if numero_final % 2 == 1: # Si el numero es impar, suma uno porque la funcion range no coge el ultimo numero
    numero_final += 1

lista_numeros = []
for numero in range(numero_inicial, numero_final, 2):
    lista_numeros.append(numero)

print(lista_numeros)