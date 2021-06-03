from utils.utils import Data

import numpy as np
from skimage import data, img_as_float
import matplotlib.pyplot as plt

class Picture:
	def __init__ (self, IMAGE):
		# load pic...
		print ("Loading picture...")
		self.picData = IMAGE

		# load shape of image
		#self.rows, self.cols = IMAGE.shape




	# compute SSIM 
	def __add__ (self, pic_Y):
		# init data
		#X_D = self.picData.tolist ()
		#Y_D = pic_Y.picData.tolist ()

		# compute data
		X = Data (self.picData.ravel ())
		Y = Data (pic_Y.picData.ravel ())
		cov = X + Y

		# compute constants
		L = self.picData.max () - self.picData.min ()
		C1 = (0.01 * L) ** 2
		C2 = (0.03 * L) ** 2

		# compute ssim for the window assigned
		result1_1 = (2*X.AVG*Y.AVG + C1)
		result1_2 = (2*cov + C2)
		#print ("The result1 is:")
		#print (result1_1, result1_2)
		result1 = result1_1 * result1_2

		result2_1 = (X.AVG**2 + Y.AVG**2 + C1)
		result2_2 = (X.VAR + Y.VAR + C2)
		#print ("The result2 is:")
		#print (result2_1, result2_2)
		result2 = result2_1 * result2_2

		#SSIM_LIST.append (result)
		# ---------------------------------------------loop


		# after quiting the loop...open image
		#SSIM_AVG = sum (SSIM_LIST) / len (SSIM_LIST)
		return result1 / result2


