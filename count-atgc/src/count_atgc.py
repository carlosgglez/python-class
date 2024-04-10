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

# Te dejo una versión de código más simple, aún no hemos visto métodos en clase, pero son una cosa maravillosa que permite que puedas hacer un monton de cosas 
# En este caso usé el método count:
with open(archivo, 'r') as f:
    DNA = f.read()
# Obtenemos la frecuencia de aparicion de cad aletra.
print(f"El total por base es: A:{ADN.count('A')} C:{ADN.count('C')} T:{ADN.count('T')} G:{ADN.count('G')}")

# En general tú código está muy bien.
```
