'''
Count ATGC
       
VERSION

1

AUTHOR

Carlos García

DESCRIPTION
Este un  script que cuenta cuantas veces a parece "A", "T", "G", "C" de una secuencia de DNA que se encuentre en un archivo.

CATEGORY


USAGE

    % python count-atgc [-parameter] [parameter_value]
    

ARGUMENTS


METHOD


SEE ALSO


ALL


import argparse

def main():

        parser = argparse.ArgumentParser(description="Lee el archivo de entrada y salida")

        #Se agrega un argumento posicional para el archivo de entrada.
        parser.add_argument("input_file", type=str, help ="El archivo de texto que se quiere procesar.")

        #Se agrega un argumento opcional para el archivo de salida.
        #"out.txt" como nombre de archivo por defecto.
        parser.add_argument ("o", "--output", type=str, default="out.txt", help='El archivo en el cual se guardara la salida del programa, por defecto se llama "out.txt"')


        args=parser.parse_args()
        with open(args.input_file, 'r') as f:
                DNA = f.read()
        print(f"El total por base es: A:{DNA.count('A')} C:{DNA.count('C')} T:{DNA.count('T')} G:{DNA.count('G')}")


````
