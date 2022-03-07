from functools import reduce


def esImpar(num):
    if num % 2 == 1:
        return True
    return False


# Uso de filter
listaNumeros = [numero for numero in range(15, 26)]
listaImpares = list(filter(esImpar, listaNumeros))
print(f'Los numeros impares de la lista son: {listaImpares}')

# Uso de reduce
sumaImpares = reduce(lambda num1, num2: num1 + num2, listaImpares)
print(f'La suma de los numeros filtrados es: {sumaImpares}')
