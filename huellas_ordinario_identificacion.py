#!/usr/bin/env python

import os

directory=os.path.join("/home/daniel/Desktop/proyecto")

for root,dirs,files in os.walk(directory):
	for file in files:
		if file.endswith(".txt"):           
			print "encontrado"


