'''
Count ATGC
       
VERSION


AUTHOR

Carlos García

DESCRIPTION
        

CATEGORY
        

USAGE

    % python count-atgc [-parameter] [parameter_value]
    

ARGUMENTS


METHOD


SEE ALSO


        
'''


# ===========================================================================
# =                            imports
# ===========================================================================





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions
# ===========================================================================





# ===========================================================================
# =                            main
# ===========================================================================


# step 1.


# step 2.


# step 3.



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
