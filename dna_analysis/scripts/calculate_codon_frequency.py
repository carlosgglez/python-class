'''
calculate_codon_frecuency.py: Script elaborado para contar el contenido de cada codon (NNN) en una secuencia de DNA.

Este script lee una secuencia de ADN desde un archivo dado y calcula el porcentaje de aparicion de cada codon
en esa secuencia. La secuencia de ADN debe estar en un archivo de texto y solo
contener los caracteres 'A', 'C', 'G' o 'T'.

Uso:
    python calculate_codon_frequency.py <path_to_dna_file>

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.

'''

import argparse
from utils.file_io import read_dna_sequence
from operations.codon_frequency import calculate_codon_frequency


parser = argparse.ArgumentParser(description = "Script que calcula la frecuencia de codones")

parser.add_argument("--input_file",
                    type = str,
                    help = "Nombre del archivo a evaluar")

args = parser.parse_args()

#Se llama a la funcion read_dna_sequence que fue importada con anterioridad, esto para validar la secuencia de DNA
DNA = read_dna_sequence(args.input_file)

#Se calcula la frecuencia de los codones llamando a la funcion calculate_codon_frequency, la cual fue importada con aterioridad.
Frecuencies = calculate_codon_frequency(DNA)

#Una vez calculadas las frecuencias de cada codon son impresas en pantalla
print(Frecuencies)

#Se comprueba que el script se ejecute como principal
if __name__ == "__main__":
    print("Se ejecuta como script principal")