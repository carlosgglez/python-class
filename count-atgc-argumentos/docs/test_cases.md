# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrolado para calcular la cantidad de "A", "T", "G" y "C" de una secuencia de un archivo. El objetivo es validar y garantizar que el script funciona correctamente y cumple especificaciónes.
Los casos de´prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles eerores que pueden surgir.
El script esta diseñado para leer secuencias desde un archivo proporcionado como entrada.
A continuación, se presentan los detalles de los casos d prueba.


### Caso de prueba 1: Comprobación del conteo de  los nucleótidos 
- Descripción: Verificar que el script puede contar cada nucleótido de la secuencia de manera correcta
- Datos de entrada: Archivo con la secuencia "AAAGGGTTTCCCCTAGGCTA"
- Resultado esperado: Ocurrencia d las letras en el archivo:
			- A: 5
			- T: 5
			- G: 5
			- C: 5


### Caso de prueba 2: Comprobación de error para letras distintas de los nucleótidos

- Descripción: Verificar que el script maneja correctamente los datos que son distintos a "A", "T", "G", "C".
- Datos de entrada: Archivo con los siguientes datos "esternocleidomastoideo, 15677"
- Resultado esperado: Ocurrio un error


### Caso de prueba 3: Comprobación de error para rchivo no existente
- Descripción: Verificar que el script maneja correctamente los archivos no existentes.
- Datos de entrada: Ruta a un archivo que no existe.
- Resultado esperado: El archivo no se encontró
