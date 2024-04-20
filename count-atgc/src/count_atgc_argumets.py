"""""
Count ATGC with arguments 
       
VERSION

1

AUTHOR

Carlos García

DESCRIPTION
Este un  script que cuenta cuantas veces a parece "A", "T", "G", "C" de una secuencia de DNA que se encuentre en un archivo.
El script permite seleccionar un nucleotido en especifico para contar, si no se da ninguno, por defeult contara los 4.
También tiene manejo de excepciones.

CATEGORY

Herramienta que cuenta los nucleótidos de una secuencia de DNA que proviene de un archivo.


USAGE

    % python count-atgc-arguments.py
    

ARGUMENTS

Argumento posicional =  ("input_file", type=str, help ="El archivo de texto que se quiere procesar.")
Argumento opcional= ("-n", "--nucleotide", type=str, choices=["A","T", "G", "C"], default="ATGC", help='El o los nucleótidos que quieras contar, por default son ATGC')

METHOD



SEE ALSO


ALL
"""
# ===========================================================================
# =                           libreria
# ===========================================================================

import argparse

# ===========================================================================
# =                            main
# ===========================================================================


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

