#! /usr/bin/python
#!encoding: UTF-8

import matplotlib.pyplot as pl
pl.rc('text', usetex=True)
pl.rc('font', family='Bookman')

name = raw_input("Introduzca el nombre del fichero para lectura: ")
f = open(name, "r")
X = []
Y = []

while (True):
    l = f.readline().rstrip()
    if (l == ""):
        break
    elif (l == "Número de intervalos"):
        s = f.readline().rstrip()
        X = X + [s]
    elif (l == "Tiempo de uso de CPU"):
        s = f.readline().rstrip()
        Y = Y + [s]
    else:
        pass

K = [1, 2, 3, 4, 5]
pl.plot(K,Y,'ro--')

pl.xticks([1,2,3,4,5], [r'$10$',r'$10^{2}$',r'$10^{3}$',r'$10^{4}$',r'$10^{5}$'])

pl.title('Coste computacional para aproximar $\pi$') 
pl.xlabel('Cantidad de intervalos')
pl.ylabel('Tiempo de uso de CPU (s)')

pl.xlim(0,6)
pl.ylim(-1,17)

pl.savefig("CPUtime.eps", dpi=72)
pl.show()

