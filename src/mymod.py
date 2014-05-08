#! /usr/bin/python
#!encoding: UTF-8

import sys
import time

# Función destinada a calcular el valor aproximado del número pi.
def aprox (n):
    suma = 0.0
    for i in range (1, int(n+1)):
        xi = (i-0.5)/n
        fxi = 4/(1+xi**2)
        suma += fxi
    pi = suma/n 
    return pi

# Función destinada a la detección de errores.
def error (n, t, umbral, ref):
    warn = 0.0
    ref = aprox(n)
    for j in range (1, t+1):
        pi = aprox(j*n)
        if (abs(pi - ref) > umbral):
            warn += 1
    return (warn/t) * 100

# Función destinada a almacenar los resultados del experimento en un fichero.
def save (name, intervalos, umbrales):
    PI = 3.1415926535897931159979634685441852
    num_iter = 10   # Número de comprobaciones en cada llamada a la función "error".
    t0 = time.time()   # Referencia para medir el tiempo total de ejecución
    c0 = time.clock()  # Referencia para medir el tiempo de uso de CPU
    f = open(name, "w")
    
    for i in range (len(intervalos)):
        f.write("Número de intervalos" + "\n" + str(intervalos[i]) + "\n")
        t0 = time.time()   # Referencia para medir el tiempo total de ejecución
        c0 = time.clock()  # Referencia para medir el tiempo de uso de CPU

        for j in range (len(umbrales)):
            f.write("Umbral de error" + "\n" + str(umbrales[j]) + "\n")
            pcent = error(intervalos[i], num_iter, umbrales[j], PI)
            f.write("Porcentaje de fallos" + "\n" + str(pcent) + "\n")
        
        tf = time.time() - t0
        cf = time.clock() - c0
        f.write("Tiempo total de ejecución" + "\n" + str(tf) + "\n")
        f.write("Tiempo de uso de CPU" + "\n" + str(cf) + "\n")
    f.close()

if __name__ == "__main__":
    PI = 3.1415926535897931159979634685441852
    intervalos = (1e1, 1e2, 1e3, 1e4, 1e5))
    umbrales = (1e-3, 1e-4, 1e-5, 1e-6, 1e-7)
    fname = raw_input("Nombre deseado para el fichero de salida: ")
    save(fname, intervalos, umbrales)
    print "Operación realizada con éxito."


