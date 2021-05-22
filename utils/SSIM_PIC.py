from utils import Data
class Picture:
	def __init__ (self, fileName):
		# load pic...
		self.picData = getPic (fileName)

		# check shape of array FIXME



	# compute SSIM 
	def __add__ (self, pic_Y):
		SSIM_LIST = []
		# loop---------------------------------------------
		# select a window of size 11*11 (pixel*pixel)
		window_X = ?
		window_Y = ?

		# init data
		X = Data (window_X)
		Y = Data (window_Y)
		cov = X + Y

		# compute ssim for the window assigned
		result = ((2*X.AVG*Y.AVG)*(2*cov))/((X.AVG**2 + Y.AVG**2)*(X.VAR + Y.VAR))
		SSIM_LIST.append (result)
		# ---------------------------------------------loop


		# after quiting the loop...
		SSIM_AVG = sum (SSIM_LIST) / len (SSIM_LIST)
		return SSIM_AVG


	# static function
	## get image file by filename FIXME
	def getPic (fileName):	
