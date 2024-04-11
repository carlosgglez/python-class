#  Count ATGC 

Este es un script de Python diseñado para leer un archivo, el que sea de su interes, que contenga una secuencia de un genoma y contar todas "A", "T", "G" y "C" que tenga dicha secuencia.

## Uso

El script acepta que se introduzca el nombre del archivo para poder abrirlo y permite establecer el nombre para un archivo de salida o por default sera "output.txt".

```
parser = argparse.ArgumentParser(description="Lee el archivo de entrada y salida")

#Se agrega un argumento posicional para el archivo de entrada.

parser.add_argument("input_file", type=str, help ="El archivo de texto que se quiere procesar.")

#Se agrega un argumento opcional para el archivo de salida.
#"out.txt" como nombre de archivo por defecto.
parser.add_argument ("-o", "--output", type=str, default="out.txt", help='El archivo en el cual se guardara la salida del programa, por defecto se llama "out.txt"')

```


## Salida

El script creara un archivo en el cual contendra la frecuencia de apariciones de cada nucleotido.
El archivo de salida puede ser nombrado como gustes, o por default sera "output.txt".

## Control de errores

Si el archivo proporcionado no existe, el script generará un mensaje de error. Del mismo modo, si el archivo tiene algun error, el script generará un error.

## Pruebas

El script incluye un conjunto de pruebas unitarias.

## Datos

El script esta diseñado para trabajar con texto plano, no importa la longitud de las secuencias ni su orden.

## Metadatos y documentacion

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script.

## Codigo fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Terminos de uso

Este script está disponible bajo la licencia MIT license. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor citelo.

## Contactenos

