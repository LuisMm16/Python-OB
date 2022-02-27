# Encontrar si un numero es primo o no

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0: # Verifica si es par para eliminar mitad de posibilidades
        return False
    else:
        for x in range(3, numero, 2):
            if numero % x == 0:
                return False
        return True

#Pruebas:
print(es_primo(1546781519841238))
print(es_primo(73))
print(es_primo(49979693))