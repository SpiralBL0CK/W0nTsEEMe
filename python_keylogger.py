import keyboard
from types import *
from stat import *
import os
import sys
import psutil
list = [65,66,67,68,69,70,97]
fisier = '1.txt'
def get_cpu_procentage():
	try:
		fd = open('info.txt',"w+")
		cpu_procent = psutil.cpu_percent()
		fd.write(str(cpu_procent))
		fd.write("\n");
		fd.write(str(psutil.virtual_memory()))
	
	except IOError:
		os.system("touch info.txt")

#get_cpu_procentage()

while True:
	for i in list:	
		try:
			 fd = open(fisier,'S_IWUSR')
			 if keyboard.is_pressed(str(unichr(i))):
				print (str(chr(i))) #"test for seing the output of key pressed"
	      		 	#fd.write(str(unichr(i))).join
				

		except IOError:
			os.system("touch 1.txt")

