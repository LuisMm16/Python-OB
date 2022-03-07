listaPaises = input('Ingrese la lista de paises separados por una coma: ').split(',')
listaPaises = [pais.capitalize() for pais in listaPaises]
print(listaPaises)
listaPaises = sorted(set(listaPaises))
print(f'La lista de paises: {", ".join(listaPaises)}')
