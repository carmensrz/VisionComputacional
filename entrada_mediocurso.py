#!/usr/bin/env python
 
import Image, sys

f = open("ImagenBinaria.txt", "w") #Se crea archivo para guardar la imagen en binario
g = open("ImagenColores.txt", "w") #Se crea archivo para guardar los colores en RGB de cada pixel de la imagen

x = 1
y = 1
lista = []
sum = 0
im = Image.open("img8.png") 
Ancho=178
Largo=140


for y in range(0,Ancho): #Ancho
	for x in range(0,Largo): #Largo
		pix = im.load()
		pix[x, y]
                if pix[x,y] == (255,255,255): #Color Blanco en RGB
	       	        c= 1
		else:
			c= 0
		f.write(str(c))
	f.write('\n')

var = im.getcolors()
g.write(str(var))