# Count ATGC

Fecha: 04/04/2024

**Participantes**:

- Carlos García González <email: carlosgg@lcg.unam..mx>

## Descripción del Problema

Este es un programa que sirve para contar las  ocurrencias de "A", "T", "C" Y "G" de un archivo. La necesidad surge del requerimiento de análisi de secuencias donde se ocupa contar cuantos nucleótidos contiene la secuencia de  manera rapida y eficaz.
El problema enunciado implica leer los nucleótidos de un archivo, contar cuantas veces se repite cada uno y luego mostrar el total de cada uno.

## Especificación de Requisitos

Requisitos funcionales

- Leer los nucleótidos de un archivo dado, solo si estan en mayusculas
- Calcular las repeticiones de cada nucleótido
- Desplegar un mensaje de error si el archivo no existe
- Desplegar un mensaje de error si los datos de entrada estan en otro formato

Requisitos no funcionales

- El script debe de estar escrito en Python
- El tiempo de respuesta debe de ser rápido, incluso con archivos de gran tamaño
- La entrada del archivo debe de ser flexible

## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en Python, así como el manejo de excepciones para la validación de datos y archivo. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

```
def contar_ocurrencias_letras(archivo):
    ocurrencias = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    with open(archivo, 'r') as f:
        for linea in f:
            for letra in linea:
                if letra.upper() in ocurrencias:
                    ocurrencias[letra.upper()] += 1
    return ocurrencias

def main():
    nombre_archivo = input("Por favor, introduce el nombre del archivo: ")
    try:
        resultado = contar_ocurrencias_letras(nombre_archivo)
        print("Ocurrencias de las letras en el archivo:")
        for letra, cantidad in resultado.items():
            print(f"{letra}: {cantidad}")
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()

```

Èl formatp de los datos será simplemente un archivo.


#### Caso de uso


```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-------+-------+
         |   Sumador de  |
         |   Números en  |
         |   Archivo     |
         | (Sistema)     |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo de entrada con una secuencia para contar sus nucleótidos. El sistema valida el archivo y los datos de entrada, calcula la repetición de cada nucleótido y muestra el resultado.
- **Flujo principal**:

        1. El actor inicia el sistema proporcionando el archivo de entrada con los números a sumar.
        2. El sistema valida el archivo y los datos de entrada.
        3. El sistema calcula la catidad de cada nucleotido.
        4. El sistema muestra el resultado.

- **Flujos alternativos**:
        - Si el archivo proporcionado no existe
                1. El sistema muestra un mensaje de error.
        - Si los datos de entrada no son nucleótidos en mayusculas
                1. El sistema muestra un mensaje de error.
