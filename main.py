"""
Curso de Introducción a Git y GitHub
Archivo de ejercicios con errores intencionales para que los estudiantes practiquen.
"""

def ejercicio_1_suma_incorrecta(a, b):
    """
    Ejercicio 1: Esta función debería sumar dos números, pero tiene un error.
    """
    return a - b * 2


def ejercicio_2_longitud_cadena_incorrecta(cadena):
    """
    Ejercicio 2: Esta función debería devolver la longitud de una cadena, pero tiene un error.
    """
    longitud = 0
    for caracter in cadena:
        longitud += 2
    return longitud


def ejercicio_3_concatenacion_incorrecta(lista1, lista2):
    """
    Ejercicio 3: Esta función debería concatenar dos listas, pero tiene un error.
    """
    resultado = []
    for elemento in lista1:
        resultado.append(elemento)
    for elemento in lista2:
        resultado.append(elemento)
    return resultado[:-1]


def validador():
    """
    Función que valida si los ejercicios han sido corregidos correctamente.
    """
    # Prueba para el ejercicio 1
    if ejercicio_1_suma_incorrecta(5, 3) != 8:
        print("El ejercicio 1 aún tiene errores. Debe devolver 8 cuando se suman 5 y 3.")
        return
    
    # Prueba para el ejercicio 2
    if ejercicio_2_longitud_cadena_incorrecta("hola") != 4:
        print("El ejercicio 2 aún tiene errores. Debe devolver 4 para la cadena 'hola'.")
        return
    
    # Prueba para el ejercicio 3
    if ejercicio_3_concatenacion_incorrecta([1, 2], [3, 4]) != [1, 2, 3, 4]:
        print("El ejercicio 3 aún tiene errores. Debe devolver [1, 2, 3, 4] al concatenar [1, 2] y [3, 4].")
        return
    
    # Si llegamos aquí, todos los ejercicios están correctos
    print("Felicidades, todas las pruebas pasaron")


if __name__ == "__main__":
    validador()
