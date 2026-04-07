# Identificador de longitud de palabras
print("Longitud de una frase")

while True:
    palabra = input("Introduce una palabra que contenga de 4 a 8 letras: ")

    # Validar que solo sean letras
    if not palabra.isalpha():
        print("Entrada inválida. Solo se permiten letras.")
        continue

    # Validar longitud mínima
    if len(palabra) < 4:
        print(f'Hacen falta letras. Solo tiene {len(palabra)} letras')
    # Validar longitud máxima
    elif len(palabra) > 8:
        print(f'Sobran letras. Tiene {len(palabra)} letras')
    else:
        print(f'La palabra: {palabra} es correcta.')
        break

#==========================================================================

# ----Diccionario de cuadrantes----
cuadrantes = {
    '+,+': 'Cuadrante I',
    '-,+': 'Cuadrante II',
    '-,-': 'Cuadrante III',
    '+,-': 'Cuadrante IV'
}

# Función para pedir coordenadas con validación
def pedir_coordenada(nombre_eje):
    while True:
        try:
            valor = int(input(f'Introduce el valor del eje {nombre_eje}: '))
            if valor == 0:
                print("El valor no puede ser igual a 0")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Debes introducir un número entero.")

# Pedir valores
eje_x = pedir_coordenada("X")
eje_y = pedir_coordenada("Y")

# Construir clave
coordenada = ('-,' if eje_x < 0 else '+,') + ('-' if eje_y < 0 else '+')

# Mostrar resultado
print("El punto se encuentra en el " + cuadrantes[coordenada])





