import glob
import os
from PIL import Image

path=r'./static/pic/big/'
pics=glob.glob(path+'*.jpg')
for pic in pics:
	