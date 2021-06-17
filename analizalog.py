import sys
argumentos = sys.argv
cadena_tipo_log=argumentos[1]
nombre_archivo_entrada=argumentos[2]
nombre_archivo_salida=argumentos[3]
archivo_entrada_log = open (nombre_archivo_entrada,'r')
archivo_salida_log = open (nombre_archivo_salida,'w')
for linea in archivo_entrada_log:
    buscar_warn=linea.find(cadena_tipo_log)
    if buscar_warn != -1:
        archivo_salida_log.write(linea)
archivo_entrada_log.close()
archivo_salida_log.close()
