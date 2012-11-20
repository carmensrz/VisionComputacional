#!/usr/bin/env python

import os

c1 = open("Comp1.txt", "r")
c2 = open("Comp2.txt", "r")

archivoUno = c1.readlines()
archivoDos = c2.readlines()
c1.close()
c2.close()

if archivoUno == archivoDos:
	print "Es igual"
else:
	print "No es igual"


