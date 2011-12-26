import sys
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.pyplot import text, plot
import psutil as p
from os import spawnlp
from os import P_WAIT


MAXITERS = 240
percent = 0
integral = []

class CPUMonitor(FigureCanvas) :
	def __init__(self) :
		self.before = self.prepare_cpu_usage()
		self.fig = Figure()
		self.ax = self.fig.add_subplot(111)
		FigureCanvas.__init__(self, self.fig)
		self.ax.set_xlim(0, 240)
		self.ax.set_ylim(0, 100)
		self.ax.set_autoscale_on(False)
		self.usage = []
		self.l_usage, = self.ax.plot([],self.usage,label='')
		self.fig.canvas.draw()
		self.cnt = 0
		self.timerEvent(None)
		self.timer = self.startTimer(250)

	def prepare_cpu_usage(self) :
		t = p.cpu_times()
		return t.user + t.system

	def get_cpu_usage(self) :
		now = self.prepare_cpu_usage()
		delta = now - self.before
		self.before = now
		return delta*100

	def get_integral_usage(self) :
		summ = 0
		for i in self.usage :
			summ += i
		return summ

	def timerEvent(self, evt) :
		result = self.get_cpu_usage()
		self.usage.append(result)
		self.l_usage.set_data(range(len(self.usage)),self.usage)
		percent = self.get_integral_usage()
		self.fig.suptitle("Integral CPU usage: %.2f" % percent + '%', fontsize="16", backgroundcolor='gray')
		self.fig.canvas.draw()
		self.fig.suptitle('')
		if self.cnt == MAXITERS:
			self.killTimer(self.timer)
		else:
			self.cnt += 1



#main

app = QtGui.QApplication(sys.argv)
widget = CPUMonitor()
widget.setWindowTitle("A Minute of CPU Usage Updated in RealTime %.2f" % percent + '%')
widget.show()
sys.exit(app.exec_())

for i in range(1000,10000) :
	spawnlp(P_WAIT, "./solver.py", "solver.py", i)
	integral.append(percent)
	print percent
	percent = 0

plot (integral, range(1000,10000))

