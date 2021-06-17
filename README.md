# RetoArchivoLog
Solucion al reto de leer archivo de log y generar archivos de salida de logs para INFO WARN ERROR

# DESCRPCION DEL RETO
Un log es una cadena de texto que brinda información al usuario sobre una situación particular en un sistema computacional. Un log tipo WARN se caracteriza por contener la palabra WARN dentro de la cadena de texto (dentro del log). De igual forma existen logs de tipo INFO y ERROR. Un conjunto de logs se pueden agrupar en un archivo de texto plano donde cada fila corresponde a un log. Teniendo el siguiente archivo de logs (entrada.log), construya un programa en Python3 o C/C++ que le permita a un usuario extraer un log de un tipo particular y agruparlos dentro de un nuevo fichero. La interfaz tipo consola de este aplicativo en particular debe permitirle al usuario ingresar el tipo de log que desee extraer, el nombre del fichero de entrada y un nombre de fichero de salida donde se guardan los logs extraídos. EJEMPLO 1$ python3 app.py WARN entrada.log salida.log $ ./app WARN entrada.log salida.log.

# SOLUCION
El codigo de la solucion corresponde a analizalog.py  

## Ejemplos para ejecucion con Python3  
$python3 analizalog.py WARN entrada.log salidaw.log  
$python3 analizalog.py INFO entrada.log salidai.log  
$python3 analizalog.py ERROR entrada.log salidae.log  

## Ejemplos para ejecucion desde el bash de linux  
$./analizalog WARN entrada.log salidaw.log  
$./analizalog INFO entrada.log salidai.log  
$./analizalog ERROR entrada.log salidae.log  

