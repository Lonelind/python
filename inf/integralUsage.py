from matplotlib import pyplot as plot
from numpy import trapz
from os import spawnlp
from os import P_WAIT
from psutil import cpu_percent
from threading import Thread

def eqSolver (split) :
    spawnlp(P_WAIT, "./equation.py", "equation.py", str(split)) # start solving an equation

def listSum (list) :
    s = 0.
    for i in list :
        s += i
    return s

def integralSum (splitStart, splitEnd, splitStep) :
    integralUsage = []
    splits = []

    for split in xrange(splitStart, splitEnd, splitStep) :
        # thread definition
        thread = Thread(None, eqSolver, None, [ split ])
        thread.start()

        # initial condition
        cpuUsage = [ 0. ]
        
        while True :
            t = cpu_percent()
            cpuUsage.append(t)
            if not thread.is_alive() :
                break

        splits.append(split)
        integralUsage.append(trapz(cpuUsage))

    plot.plot(splits, integralUsage)
    plot.savefig('usage.png', format='png')

if __name__ == "__main__":
    integralSum(1, 10000, 100)
