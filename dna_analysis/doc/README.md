# DNA ANALYSIS
Este es un paquetre de Python diseñado para leer un archivo, el que sea de su interes, que contenga una secuencia de un genoma y apartir de ahí, puede contar todas las "A" y "T" de la secuencia o sacar la frecuencia de aparición de 
cada codon.

## Uso
Ambos script aceptan que se introduzca el nombre del archivo para poder abrirlo y leerlo.

parser = argparse.ArgumentParser(description="Lee el archivo de entrada)

#Se agrega un argumento opsional para el archivo de entrada.

parser.add_argument("-i", "--input_file", 
                    type=str, 
                    help = "El archivo de texto que se quiere procesar.",
                    requiered True)

## Salida
Dependiendo el script sera su salida, en general uno da la frecuencia de AT y el otro la frecuencia de aparicion de cada codon.

## Control de errores
Si el archivo proporcionado no existe, el script generará un mensaje de error. Del mismo modo, si el archivo tiene algun error, el script generará un error.

## Pruebas
Cada script incluye un conjunto de pruebas unitarias.

## Datos
Los script estan diseñados para trabajar con texto plano, no importa la longitud de las secuencias ni su orden.

## Metadatos y documentacion
Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script.

## Codigo fuente
El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Terminos de uso
Este script está disponible bajo la licencia MIT license. Consulte el archivo LICENSE para obtener más detalles.

## Como citar
Si utiliza este script en su trabajo, por favor citelo.

## Contactenos