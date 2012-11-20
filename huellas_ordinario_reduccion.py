#!/usr/bin/env python

import os
import glob
Arc = glob.glob("*.txt")

directory=os.path.join("/home/daniel/Desktop/proyecto")

c1 = open("Desconocido.txt", "r")
archivodesconocido = c1.readlines()

for root,dirs,files in os.walk(directory):
	for file in files:
		if file.endswith(".txt"): 
			
			c2 = open(file, "r")
			archivoencontrado = c2.readlines()
			if archivodesconocido == archivoencontrado:				
				print ("Tu eres: ", Arc[nombre])
				
						


			

