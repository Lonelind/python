from sys import argv
from math import cos
from scipy.integrate import quad
from scipy.optimize import newton

# cos(x) + (x^3)'' + (x^2)' = 0
#
h = 1. / float(argv[1])

def yi(xj,yj) :
    return yj * (1. - 2. * h) - 2. * h * cos (xj)

def xi(xj,yj) :
    return .2 * h * yj + xj

def eqSolve() :
    ta = 10.
    y = [ 1. ]
    x = [ .5 ]
    for i in xrange(int(solveRange[1] / h)) :
        y.append(newton(yi,x[i],args=(y[i]),maxiters=10000))
        x.append(newton(xi,x[i],args=(y[i]),maxiters=10000))

if __name__ == "__main__" :
    eqSolve()
