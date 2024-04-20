# Count ATGC

Fecha: 19/04/2024

**Participantes**:

- Carlos García González <email: carlosgg@lcg.unam..mx>

## Descripción del Problema

Este es un programa que sirve para contar las  ocurrencias de "A", "T", "C" Y "G" de un archivo. La necesidad surge del requerimiento de análisi de secuencias donde se ocupa contar cuantos nucleótidos contiene la secuencia de  manera rapida y eficaz.
El problema enunciado implica leer los nucleótidos de un archivo, contar cuantas veces se repite cada uno y luego mostrar el total de cada uno.

## Especificación de Requisitos

Requisitos funcionales

- Leer los nucleótidos de un archivo dado, no importa si estan en mayusculas o minusculas
- Calcular las repeticiones de cada nucleótido
- Desplegar un mensaje de error si el archivo no existe
- Desplegar un mensaje de error si los datos de entrada estan en otro formato
- Desplegar un mensaje de error si el archivo esta vacio

Requisitos no funcionales

- El script debe de estar escrito en Python
- El tiempo de respuesta debe de ser rápido, incluso con archivos de gran tamaño
- La entrada del archivo debe de ser flexible

## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en Python, así como el manejo de excepciones para la validación de datos y archivo. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

"""
import argparse

parser = argparse.ArgumentParser(description="Lee el archivo de entrada y salida")

#Se agrega un argumento posicional para el archivo de entrada.

parser.add_argument("input_file", type=str, help ="El archivo de texto que se quiere procesar.")

#Se agrega un argumento opcional para que selecione los nuceótidos que eliga el usuario
#ATGC como los nucleótidos determinados por defecto.
parser.add_argument ("-n", "--nucleotide", type=str, choices=["A","T", "G", "C"], default="ATGC", help='El o los nucleótidos que quieras contar, por default son ATGC')


args=parser.parse_args()

#Definición de una excepción especial para el programa
class FileEmptyError(Exception):
    def __init__(self, input_file):
        self.input_file = input_file
        self.message = (f"El archivo {input_file} está vacío")
        super().__init__(self.message)


#Se crean las listas nucleotios, nnucleotidos y caracteres_incorrectos con la finalidad de pode buscar caracteres incorrectos 
nucleotidos=["A", "T", "G", "C"]
nnucleotidos=["a", "t", "g", "c"]
caracteres_incorrectos=[]

#Try usado para agregar las excepciones necesarias 
try:
    with open(args.input_file, 'r') as f:
        DNA = f.read()

    if  DNA==None: #Si el archivo esta vacio entra a este if que tiene la función de crea una nueva excepcion
        raise FileEmptyError(f"{args.input_file}")

    
    for nucleotido in DNA: #for usado para revisar que todos los caracteres del archivo son correctos, si no es así los guarda en una lista vacia
        if nucleotido not in nucleotidos and nnucleotidos:
            caracteres_incorrectos.append(nucleotido)

    if caracteres_incorrectos: #if usado para imprimir los caracteres incorrectos
        print(f"El archivo {args.input_file} contiene caracteres diferentes: {' '.join(caracteres_incorrectos)}")
        
    

except FileNotFoundError: #Excepción si no se encuentra el archivo
    print(f"El archivo {args.input_file} no existe")
    exit()

except FileEmptyError as e: #Excepción creada para archivos vacios
    print (e)
    exit()

    if args.nucleotide=="A":
        print(f"El total de Adeninas es:{DNA.upper().count('A')}") 
    
if args.nucleotide=="T":
    print(f"El total de Timinas es:{DNA.upper().count('T')}")

if args.nucleotide=="G":
    print(f"El total de guaninas es:{DNA.upper().count('G')}")

if args.nucleotide=="C":
    print(f"El total de citocinas es:{DNA.upper().count('C')}")

if args.nucleotide=="ATGC":
    print(f"El total de cada base es: A:{DNA.upper().count('A')} C:{DNA.upper().count('C')} T:{DNA.upper().count('T')} G:{DNA.upper().count('G')}")


"""

El formatp de los datos será simplemente un archivo.


#### Caso de uso


```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-------+-------+
         |  Contador de  |
         | nucleotidos   |
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
        - Si los datos de entrada no son nucleotidos
                1. El sistema muestra un mensaje de error.
