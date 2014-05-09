#! /usr/bin/python
#!encoding: UTF-8

import matplotlib.pylab as pl
import numpy as np

pl.rc('text', usetex=True)

def f (x):
    return 4/(1+x**2)

X = np.linspace(0, 1, 500, endpoint=True)
Y = f(X)

pl.plot(X,Y,'b')
pl.title(r'Representaci\'on gr\'afica de la funci\'on $f(x) = \frac{4}{1+x^{2}}$ en [0, 1]') 
pl.xlabel('Valores de X')
pl.ylabel('Valores de f(x)')

pl.xlim(-0.25, 1.25)
pl.ylim(1.5, 4.5)

pl.savefig("function.eps", dpi=72)
pl.show()
