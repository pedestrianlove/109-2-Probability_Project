import math

class Data:
	def __init__ (self, data):
		self.DATA = data	# _DATA: Stores image's data array
		self.avg ()		# AVG: Stores average of the data
		self.variance ()	# VARIANCE: Stores the variance of the array
		self.stdeviation ()	# STD:	Stores the STD of the array

	def avg (self):
		self.AVG = sum (self.DATA)
		self.AVG /= len (self.DATA)

	def variance (self):
		self.VAR = 0.0
		for x in self.DATA:
			self.VAR += (x - self.AVG) ** 2

	def stdeviation (self):
		self.STD = sqrt (self.VAR)

	def __add__(self, Y):
		# compute E[X*Y]
		tmp = []
		# assuming X, Y has the same length (FIXME)
		for i in range (len (self.DATA)):
			tmp.append (self.DATA[i] * Y.DATA[i])
		cov = sum (tmp) / len (tmp)
		
		# subtracting E[x]*E[Y]
		cov -= (self.AVG * Y.AVG)
		
		# return result
		return cov

	
