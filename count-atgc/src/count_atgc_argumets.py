'''
Count ATGC with arguments 
       
VERSION

1

AUTHOR

Carlos García

DESCRIPTION
Este un  script que cuenta cuantas veces a parece "A", "T", "G", "C" de una secuencia de DNA que se encuentre en un archivo.

CATEGORY

Herramienta que cuenta los nucleótidos de una secuencia de DNA que viene de un archivo.


USAGE

    % python count-atgc-arguments.py
    

ARGUMENTS

Argumento posicional =  ("input_file", type=str, help ="El archivo de texto que se quiere procesar.")
Argumento opcional= ("-n", "--nucleotide", type=str, choices=["A","T", "G", "C"], default="ATGC", help='El o los nucleótidos que quieras contar, por default son ATGC')

METHOD



SEE ALSO


ALL

# ===========================================================================
# =                           libreria
# ===========================================================================

import argparse
#Libreria que da el modulo os que permite trabajar y manipular rutas de archivo>
import os


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

#If utilizado para revisar la existencia o no  del archivo
if not os.path.exists(args.input_file):
    print("El archivo de entrada especificado no existe.")
    exit()


with open(args.input_file, 'r') as f:
        DNA = f.read()
print(f"El total por base es: A:{DNA.count('A')} C:{DNA.count('C')} T:{DNA.count('T')} G:{DNA.count('G')}")



````
