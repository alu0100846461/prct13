#! /usr/bin/python
#!encoding: UTF-8

import matplotlib.pyplot as pl
pl.rc('text', usetex=True)
pl.rc('font', family='Bookman')

name = raw_input("Introduzca el nombre del fichero para lectura: ")
f = open(name, "r")

Y1 = []
Y2 = []
Y3 = []
Y4 = []
Y5 = []
Y = []

while (True):
    l = f.readline().rstrip()
    if (l == ""):
        break
    elif (l == "Porcentaje de fallos"):
        s = f.readline().rstrip()
        Y = Y + [s]
    else:
        pass

f.close()
X = [1, 2, 3, 4, 5]

for i in range (0, 5):
    Y1 = Y1 + [Y[i]]
for i in range (5, 10):
    Y2 = Y2 + [Y[i]]
for i in range (10, 15):
    Y3 = Y3 + [Y[i]]
for i in range (15, 20):
    Y4 = Y4 + [Y[i]]
for i in range (20, 25):
    Y5 = Y5 + [Y[i]]

pl.plot(X,Y1, color="blue", linewidth=2.5, linestyle="-", label="r$10$")
pl.plot(X,Y2, color="red", linewidth=2.5, linestyle="-", label="r$10^{2}$")
pl.plot(X,Y3, color="purple", linewidth=2.5, linestyle="-", label="r$10^{3}$")
pl.plot(X,Y4, color="green", linewidth=2.5, linestyle="-", label="r$10^{4}$")
pl.plot(X,Y5, color="black", linewidth=2.5, linestyle="-", label="r$10^{5}$")

pl.xticks([1,2,3,4,5], [r'$10^{-3}$',r'$10^{-4}$',r'$10^{-5}$',r'$10^{-6}$',r'$10^{-7}$'])

pl.title('Porcentaje de errores para distintas cantidades de intervalos') 
pl.xlabel('Cantidad de intervalos')
pl.ylabel('Porcentaje de errores')

pl.xlim(0,6)
pl.ylim(-10,100)

pl.savefig("errores.eps", dpi=72)
pl.show()

