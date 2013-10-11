import os
import sys

def dirtree(filenames):
	files=os.listdir(filenames)
	for fil in files:
		if os.path.isdir(os.path.abspath(filenames+'/'+fil)) == True:
			dirtree(os.path.abspath(filenames+'/'+fil))
		else:
			print os.path.abspath(filenames+'/'+fil)
			


dirtree(sys.argv[1])
