# Determinar si un año fue bisiesto

def año_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Pruebas:

print(año_bisiesto(2016))
print(año_bisiesto(1800))
print(año_bisiesto(1900))
print(año_bisiesto(1998))